"""vLLM client (OpenAI-compatible /v1/chat/completions)."""

from __future__ import annotations

import base64
from pathlib import Path

import httpx

_IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
_MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


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
        images: list[Path] | None = None,
        max_tokens: int | None = None,
        temperature: float | None = None,
    ) -> str:
        """Send prompt to the LLM, optionally with images for vision models."""
        if images:
            content: str | list = _build_multimodal_content(prompt, images)
        else:
            content = prompt

        body = {
            "model": self._model_name,
            "messages": [{"role": "user", "content": content}],
            "max_tokens": max_tokens or self._default_max_tokens,
            "temperature": (
                temperature if temperature is not None else self._default_temperature
            ),
            # Qwen3 ships with reasoning enabled by default and will spend the
            # entire output budget on a <think> block, leaving no JSON.
            "chat_template_kwargs": {"enable_thinking": False},
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


def _build_multimodal_content(text: str, images: list[Path]) -> list[dict]:
    """Build an OpenAI-compatible multimodal content list (text + base64 images)."""
    content: list[dict] = [{"type": "text", "text": text}]
    for img_path in images:
        suffix = img_path.suffix.lower()
        if suffix not in _IMAGE_SUFFIXES:
            continue
        mime = _MIME[suffix]
        data = base64.b64encode(img_path.read_bytes()).decode()
        content.append({
            "type": "image_url",
            "image_url": {"url": f"data:{mime};base64,{data}"},
        })
    return content
