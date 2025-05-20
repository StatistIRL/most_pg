from functools import lru_cache
from pathlib import Path
from typing import Type, TypeVar

import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)
BASE_DIR = Path(__file__).parent.parent


@lru_cache
def get_settings(cls: Type[TSettings]) -> TSettings:
    dotenv.load_dotenv(BASE_DIR / ".env")
    return cls()


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="database_")

    driver: str = "postgresql+asyncpg"
    username: str
    password: str
    host: str
    port: int
    name: str

    @property
    def url(self) -> str:
        return f"{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"
