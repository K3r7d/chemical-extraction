from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    mineru_url: str = Field("http://mineru:8000", description="MinerU service URL")
    vision_url: str = Field("http://vision:8001", description="Vision (triage + OCSR) service URL")
    chemvlm_url: str = Field("http://chemvlm:8002", description="ChemVLM (TinyChemVL) service URL")
    llm_url: str = Field(
        "http://llm:8000/v1", description="vLLM OpenAI-compatible base URL"
    )
    llm_model_name: str = Field(
        "Qwen/Qwen3.6-72B-Instruct",
        description="HF id of the model vLLM is serving",
    )
    llm_api_key: str = Field("EMPTY", description="vLLM doesn't enforce auth by default")
    llm_max_tokens: int = Field(16000, ge=1)
    llm_temperature: float = Field(0.0, ge=0.0, le=2.0)
    llm_request_timeout_s: float = Field(600.0, gt=0)

    output_dir: str = Field("outputs", description="where extraction.json files land")


def get_settings() -> Settings:
    return Settings()
