from __future__ import annotations

from pathlib import Path
from typing import Tuple, Type

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

# Absolute path — works from any working directory and inside Docker.
_CONFIG_FILE = str(Path(__file__).parents[2] / "configs" / "config.yml")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        yaml_file=_CONFIG_FILE,
        yaml_file_encoding="utf-8",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ── Service URLs ──────────────────────────────────────────────────────────
    mineru_url: str
    llm_url: str

    # ── LLM ───────────────────────────────────────────────────────────────────
    llm_model_name: str
    llm_api_key: str
    llm_max_tokens: int = Field(ge=1)
    llm_temperature: float = Field(ge=0.0, le=2.0)
    llm_request_timeout_s: float = Field(gt=0)
    llm_max_model_len: int = Field(ge=1)
    llm_dtype: str
    llm_send_images: bool = True

    # ── Service timeouts ──────────────────────────────────────────────────────
    mineru_timeout_s: float = Field(gt=0)

    # ── Pipeline ──────────────────────────────────────────────────────────────
    output_dir: str

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        # Priority: env vars > .env file > configs/config.yml
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            YamlConfigSettingsSource(settings_cls),
            file_secret_settings,
        )


def get_settings() -> Settings:
    return Settings()
