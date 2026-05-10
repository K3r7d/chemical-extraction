"""vLLM client (OpenAI-compatible /v1/chat/completions)."""

from __future__ import annotations

import httpx


class VLLMClient:
    def __init__(
        self,
        base_url: str,
        *,
        model_name: str,
        api_key: str = "EMPTY",
        timeout_s: float = 600.0,
        default_max_tokens: int = 16000,
        default_temperature: float = 0.0,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._model_name = model_name
        self._headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self._timeout = httpx.Timeout(timeout_s)
        self._default_max_tokens = default_max_tokens
        self._default_temperature = default_temperature

    async def complete(
        self,
        prompt: str,
        *,
        max_tokens: int | None = None,
        temperature: float | None = None,
    ) -> str:
        body = {
            "model": self._model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens or self._default_max_tokens,
            "temperature": (
                temperature if temperature is not None else self._default_temperature
            ),
        }
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            resp = await client.post(
                f"{self._base_url}/chat/completions",
                json=body,
                headers=self._headers,
            )
            resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    async def health(self) -> bool:
        async with httpx.AsyncClient(timeout=httpx.Timeout(5.0)) as client:
            try:
                resp = await client.get(
                    f"{self._base_url}/models", headers=self._headers
                )
                return resp.status_code == 200
            except httpx.RequestError:
                return False
