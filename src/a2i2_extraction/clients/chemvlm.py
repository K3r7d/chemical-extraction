"""HTTP client for the chemvlm service (TinyChemVL)."""

from __future__ import annotations

import httpx


class ChemVLMHTTPClient:
    """Async client for the chemvlm FastAPI service.

    Endpoint:
        POST /panel_extract  {img_path: str, prompt: str}  → {response: str}
        GET  /health                                       → {status: "ok", ...}
    """

    def __init__(
        self,
        base_url: str,
        *,
        timeout_s: float = 300.0,
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

    async def panel_extract(self, *, img_path: str, prompt: str) -> str:
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            r = await client.post(
                f"{self._base_url}/panel_extract",
                json={"img_path": img_path, "prompt": prompt},
            )
            r.raise_for_status()
            return r.json()["response"]
