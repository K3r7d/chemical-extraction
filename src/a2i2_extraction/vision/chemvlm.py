"""TinyChemVL wrapper: panel image + instruction → SMILES text.

TinyChemVL (Zhao et al., AAAI'26) is an InternVL2.5-4B checkpoint specialised
for chemistry vision: molecule recognition + reaction prediction. We invoke
it via the InternVL `.chat()` API.

Quantisation: pass `quantize="4bit"` to fit the 4B model into <4 GB VRAM
(suitable for an 8 GB consumer card). `quantize="none"` keeps fp16/bf16 for
cluster deployments.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ChemVLMResponse:
    img_path: str
    prompt: str
    response: str   # raw decoded text — Stage 5 parses this into compounds


class TinyChemVL:
    """Lazy-loading TinyChemVL model wrapper.

    Loaded at service startup, kept resident, called per-image.
    """

    DEFAULT_MODEL_DIR = "/cache/chemvlm/TinyChemVL"

    def __init__(
        self,
        *,
        model_dir: str = DEFAULT_MODEL_DIR,
        device: str | None = None,
        quantize: str = "none",      # "none" | "4bit"
        max_new_tokens: int = 512,
    ) -> None:
        self._model_dir = model_dir
        self._device = device
        self._quantize = quantize
        self._max_new_tokens = max_new_tokens
        self._model = None
        self._tokenizer = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def generate(self, img_path: str, prompt: str) -> ChemVLMResponse:
        self._load()
        pixel_values = self._preprocess(img_path)
        n_tiles = pixel_values.shape[0]
        gen_cfg = {
            "max_new_tokens": self._max_new_tokens,
            "do_sample": False,
        }
        # TinyChemVL's chat() contains `self.num_image_token = self.num_image_token // 16`
        # which mutates the model attribute in place. On the second call it becomes
        # 16//16=1 (text gets N_tiles positions) while the vision encoder still outputs
        # N_tiles×16 features → shape mismatch. Save and restore around each call.
        saved_num_image_token = self._model.num_image_token
        try:
            response = self._model.chat(
                self._tokenizer,
                pixel_values,
                prompt,
                gen_cfg,
                num_patches_list=[n_tiles],
            )
        finally:
            self._model.num_image_token = saved_num_image_token
        return ChemVLMResponse(img_path=img_path, prompt=prompt, response=response)

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _load(self) -> None:
        if self._model is not None:
            return

        import torch
        from transformers import AutoTokenizer

        # InternVL2.5's modeling files use relative imports
        # (`from .configuration_intern_vit import ...`), so they need a real
        # package context — sys.path alone won't do. transformers' own
        # trust_remote_code path also mishandles them (recursive walk reads
        # from a cache dir before sibling files are copied there). We register
        # the model directory as a synthetic package via importlib, which
        # makes the relative imports resolve correctly.
        InternVLChatConfig, InternVLChatModel = _load_internvl_classes(self._model_dir)

        # TinyChemVL's InternVLChatModel predates transformers ≥4.45, which added
        # `all_tied_weights_keys` (a dict) to the BitsAndBytesConfig quantizer path.
        # transformers uses it in two ways: `len(x) > 0` and `x.keys()` — must be dict.
        if not hasattr(InternVLChatModel, "all_tied_weights_keys"):
            InternVLChatModel.all_tied_weights_keys = property(
                lambda self: {
                    k: k for k in (getattr(self, "_tied_weights_keys", None) or [])
                }
            )

        device = self._device or ("cuda" if torch.cuda.is_available() else "cpu")
        config = InternVLChatConfig.from_pretrained(self._model_dir)

        kwargs: dict = {
            "config": config,
            "low_cpu_mem_usage": True,
        }
        if self._quantize == "4bit":
            from transformers import BitsAndBytesConfig
            kwargs["quantization_config"] = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
            )
            # bitsandbytes places weights on cuda itself; don't .to()
        else:
            kwargs["torch_dtype"] = torch.bfloat16

        model = InternVLChatModel.from_pretrained(self._model_dir, **kwargs).eval()
        if self._quantize != "4bit" and device == "cuda":
            model = model.cuda()

        self._tokenizer = AutoTokenizer.from_pretrained(
            self._model_dir, trust_remote_code=True, use_fast=False
        )
        self._model = model
        self._device = device

    def _preprocess(self, img_path: str):
        """InternVL2.5 dynamic-tile preprocessing → (N_tiles, 3, 448, 448) tensor."""
        import torch
        from PIL import Image
        from torchvision.transforms import functional as TF

        img = Image.open(img_path).convert("RGB")
        # Dynamic tiling: split long edge into 448-px tiles, max 12 tiles.
        # InternVL2.5's standard preprocessing — see model card.
        tiles = _dynamic_tile(img, tile_size=448, max_tiles=12)
        pixel_values = torch.stack([
            TF.normalize(
                TF.to_tensor(t),
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            )
            for t in tiles
        ])
        if self._quantize == "4bit":
            return pixel_values.to(torch.bfloat16).cuda()
        return pixel_values.to(torch.bfloat16).to(self._device)


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _dynamic_tile(img, *, tile_size: int = 448, max_tiles: int = 12) -> list:
    """InternVL2.5 dynamic preprocessing.

    Picks an aspect-ratio-preserving grid of 448-px tiles up to max_tiles,
    plus one full-image thumbnail tile. Returns PIL.Image list.
    """
    w, h = img.size
    aspect = w / h
    # Find the (cols, rows) grid that best matches the image aspect ratio.
    best = (1, 1)
    best_diff = float("inf")
    best_tiles = 1
    for n in range(1, max_tiles + 1):
        for cols in range(1, n + 1):
            if n % cols != 0:
                continue
            rows = n // cols
            grid_aspect = cols / rows
            diff = abs(grid_aspect - aspect)
            if diff < best_diff or (diff == best_diff and n > best_tiles):
                best = (cols, rows)
                best_diff = diff
                best_tiles = n

    cols, rows = best
    target_w = cols * tile_size
    target_h = rows * tile_size
    resized = img.resize((target_w, target_h))
    tiles = []
    for r in range(rows):
        for c in range(cols):
            box = (c * tile_size, r * tile_size, (c + 1) * tile_size, (r + 1) * tile_size)
            tiles.append(resized.crop(box))
    # Always append a thumbnail of the full image when there are >1 tiles.
    if cols * rows > 1:
        tiles.append(img.resize((tile_size, tile_size)))
    return tiles


_INTERNVL_PKG_NAME = "_chemvlm_internvl_pkg"


def _load_internvl_classes(model_dir: str):
    """Register the model dir as a synthetic Python package, then import.

    Returns (InternVLChatConfig, InternVLChatModel).

    Why this exists: InternVL2.5's `.py` files use relative imports
    (`from .configuration_intern_vit import ...`). For those to resolve we
    need a real package, not just sys.path. We synthesise one with
    `importlib.util` so the directory name is irrelevant and we don't need
    to write into the cached model directory.
    """
    import importlib
    import importlib.util
    import sys
    from pathlib import Path

    model_path = Path(model_dir)

    # If a previous load registered the package, just import the submodules.
    if _INTERNVL_PKG_NAME not in sys.modules:
        spec = importlib.util.spec_from_loader(_INTERNVL_PKG_NAME, loader=None)
        # Mark this as a package and tell Python where to look for submodules.
        spec.submodule_search_locations = [str(model_path)]
        pkg = importlib.util.module_from_spec(spec)
        pkg.__path__ = [str(model_path)]
        sys.modules[_INTERNVL_PKG_NAME] = pkg

    config_mod = importlib.import_module(f"{_INTERNVL_PKG_NAME}.configuration_internvl_chat")
    model_mod = importlib.import_module(f"{_INTERNVL_PKG_NAME}.modeling_internvl_chat")
    return config_mod.InternVLChatConfig, model_mod.InternVLChatModel


def resolve_model_dir(model_dir: str | Path) -> Path:
    """Confirm the model directory exists and contains config.json."""
    p = Path(model_dir)
    if not (p / "config.json").exists():
        raise FileNotFoundError(
            f"TinyChemVL config.json not found in {p}. "
            "Download via ModelScope: snapshot_download('Noct25/TinyChemVL')."
        )
    return p
