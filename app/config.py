from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    isil_env: str = "development"
    isil_debug: bool = True
    isil_host: str = "0.0.0.0"
    isil_port: int = 8000
    isil_secret_key: str = "dev-secret-change-me"

    database_url: str = f"sqlite+aiosqlite:///{ROOT_DIR / 'isil.db'}"

    isil_master_api_key: str = "dev-master-key-change-in-production"

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    perspective_api_key: str = ""
    huggingface_api_token: str = ""
    huggingface_toxicity_model: str = "unitary/toxic-bert"
    huggingface_scam_model: str = "michellejieli/emotion_text_classifier"

    use_mock_adapters_when_no_keys: bool = True
    enable_context_intelligence: bool = True
    enable_risk_memory: bool = True
    context_only_on_borderline: bool = True
    borderline_min_score: int = 35
    borderline_max_score: int = 75

    fusion_config_path: str = "config/fusion_weights.json"
    thresholds_config_path: str = "config/thresholds.json"
    policies_dir: str = "app/policies"

    @property
    def fusion_path(self) -> Path:
        return ROOT_DIR / self.fusion_config_path

    @property
    def thresholds_path(self) -> Path:
        return ROOT_DIR / self.thresholds_config_path

    @property
    def policies_path(self) -> Path:
        return ROOT_DIR / self.policies_dir

    def has_openai(self) -> bool:
        return bool(self.openai_api_key.strip())

    def has_perspective(self) -> bool:
        return bool(self.perspective_api_key.strip())

    def has_huggingface(self) -> bool:
        return bool(self.huggingface_api_token.strip())


@lru_cache
def get_settings() -> Settings:
    return Settings()
