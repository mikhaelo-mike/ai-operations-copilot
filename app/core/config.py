from functools import lru_cache
from pydantic_settings import BaseSettings , SettingsConfigDict

class settings(BaseSettings):
    app_name : str = "AI Operations Copilot"
    app_version : str = "0.1.0"
    environment : str = "Development"
    debug : bool = True
    log_level : str = "INFO"

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive = False
    )

@lru_cache
def get_settings() -> settings:
    return settings()