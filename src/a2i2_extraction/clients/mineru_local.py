"""Local MinerU 3.x client.

Shells to the `mineru` CLI bundled in our uv venv. Pipeline backend uses
PyTorch-based OCR (no PaddlePaddle package required) and auto-detects GPU
via torch.cuda.is_available(). Prerequisite: run `mineru-models-download
-s huggingface -m pipeline` once to pre-cache all 22 OCR weight files;
missing models cause silent hangs at runtime.

Output layout from MinerU 3.x:
    <output_dir>/<pdf_stem>/auto/<pdf_stem>.md
    <output_dir>/<pdf_stem>/auto/images/*.jpg
"""

from __future__ import annotations

import asyncio
import os
import shutil
import sys
import tempfile
from pathlib import Path

from .base import ParsedDocument, ParsedFigure


def _find_mineru() -> str:
    """Prefer the binary in the same venv as this Python process."""
    candidate = Path(sys.executable).parent / "mineru"
    if candidate.exists():
        return str(candidate)
    found = shutil.which("mineru")
    if found:
        return found
    raise RuntimeError(
        "mineru CLI not found. Install with: uv add 'mineru[pipeline]'"
    )


class MinerULocalClient:
    def __init__(
        self,
        *,
        backend: str = "pipeline",
        method: str = "auto",
        lang: str = "en",
        timeout_s: float = 600.0,
        output_root: Path | None = None,
    ) -> None:
        """
        Args:
            output_root: If provided, MinerU writes to a stable per-PDF subdir
                here (so figure images persist between runs and downstream
                vision tools can re-read them). If None, uses a TemporaryDirectory.
        """
        self._mineru_bin = _find_mineru()
        self._backend = backend
        self._method = method
        self._lang = lang
        self._timeout_s = timeout_s
        self._output_root = output_root

    async def parse(self, pdf_path: Path) -> ParsedDocument:
        if self._output_root is not None:
            self._output_root.mkdir(parents=True, exist_ok=True)
            return await self._parse_into(pdf_path, self._output_root)

        with tempfile.TemporaryDirectory(prefix="mineru_") as tmp:
            return await self._parse_into(pdf_path, Path(tmp))

    async def _parse_into(self, pdf_path: Path, out_dir: Path) -> ParsedDocument:
        env = os.environ.copy()
        # Force explicit device so MinerU doesn't silently fall back to CPU.
        # Auto-detection reads torch.cuda.is_available() — same result, but
        # explicit makes debugging easier and survives env edge cases.
        if "MINERU_DEVICE_MODE" not in env:
            import torch
            if torch.cuda.is_available():
                env["MINERU_DEVICE_MODE"] = "cuda"
        proc = await asyncio.create_subprocess_exec(
            self._mineru_bin,
            "-p", str(pdf_path),
            "-o", str(out_dir),
            "-b", self._backend,
            "-m", self._method,
            "-l", self._lang,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )
        try:
            _, stderr = await asyncio.wait_for(proc.communicate(), timeout=self._timeout_s)
        except TimeoutError as e:
            proc.kill()
            await proc.wait()
            raise RuntimeError(f"mineru timed out after {self._timeout_s}s on {pdf_path}") from e

        if proc.returncode != 0:
            tail = stderr.decode("utf-8", errors="replace")[-2000:]
            raise RuntimeError(
                f"mineru failed (exit {proc.returncode}) for {pdf_path}:\n{tail}"
            )

        stem = pdf_path.stem
        md_path = out_dir / stem / "auto" / f"{stem}.md"
        images_dir = out_dir / stem / "auto" / "images"

        if not md_path.exists():
            # Fallback search — MinerU layout has shifted across versions before.
            md_candidates = list(out_dir.rglob("*.md"))
            if not md_candidates:
                raise RuntimeError(
                    f"mineru produced no markdown for {pdf_path} (looked in {out_dir})"
                )
            md_path = md_candidates[0]
            images_dir = md_path.parent / "images"

        text = md_path.read_text(encoding="utf-8", errors="replace")
        figures = _collect_figures(images_dir) if images_dir.exists() else []
        return ParsedDocument(
            text=text,
            figures=figures,
            source_path=pdf_path,
            output_dir=md_path.parent,  # the auto/ dir; contains content_list.json + images/
        )

    async def health(self) -> bool:
        return Path(self._mineru_bin).exists()


def _collect_figures(images_dir: Path) -> list[ParsedFigure]:
    """Wrap image files as ParsedFigure entries.

    MinerU's pipeline backend does not emit per-figure bbox/page metadata to
    the markdown — figures are referenced by hash filename only. We surface the
    files as figures with a placeholder bbox; downstream vision stages match
    them back to markdown via the ![](images/HASH.jpg) reference.
    """
    return [
        ParsedFigure(page=-1, bbox=(0, 0, 0, 0), image_path=p, caption=None)
        for p in sorted(images_dir.iterdir())
        if p.suffix.lower() in (".jpg", ".jpeg", ".png")
    ]
