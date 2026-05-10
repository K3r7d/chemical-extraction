"""HTTP client for the vision service (SigLIP 2 triage + MolNexTR OCSR).

The vision service exposes:
    POST /triage   {output_dir: str}           → list of TriageResult dicts
    POST /ocsr     {img_paths: list[str]}       → list of OCSRResult dicts
    GET  /health                                → {"status": "ok"}
"""

from __future__ import annotations

from pathlib import Path

import httpx


class VisionClient:
    def __init__(
        self,
        base_url: str,
        *,
        timeout_s: float = 120.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout_s

    async def health(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                r = await client.get(f"{self._base_url}/health")
                return r.status_code == 200
        except Exception:
            return False

    async def triage(self, output_dir: Path) -> list[dict]:
        """Classify all images in a MinerU auto/ directory.

        Args:
            output_dir: absolute path to the auto/ dir inside the shared volume.

        Returns:
            List of dicts matching TriageResult fields.
        """
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            r = await client.post(
                f"{self._base_url}/triage",
                json={"output_dir": str(output_dir)},
            )
            r.raise_for_status()
            return r.json()["results"]

    async def ocsr(self, img_paths: list[Path]) -> list[dict]:
        """Run MolNexTR OCSR on a list of image paths inside the shared volume.

        Args:
            img_paths: absolute paths to kept chemistry images.

        Returns:
            List of dicts matching OCSRResult fields.
        """
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            r = await client.post(
                f"{self._base_url}/ocsr",
                json={"img_paths": [str(p) for p in img_paths]},
            )
            r.raise_for_status()
            return r.json()["results"]
