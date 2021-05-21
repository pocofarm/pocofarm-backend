from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    env: str = "dev"
    redoc_url: Optional[str] = "/redoc"
    docs_url: Optional[str] = "/docs"


settings = Settings()
