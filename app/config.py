import secrets
from typing import Any

from pydantic import PostgresDsn, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.constants import Environment


class CustomBaseSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


class Config(CustomBaseSettings):
    DATABASE_URL: PostgresDsn
    DATABASE_POOL_SIZE: int = 16
    DATABASE_POOL_TTL: int = 60 * 20  # 20 minutes
    DATABASE_POOL_PRE_PING: bool = True

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str] = ["*"]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str] = ["*"]

    SECRET_KEY: str = secrets.token_urlsafe(32)

    # 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str

    APP_VERSION: str = "0.1"

    @model_validator(mode="after")
    def validate_sentry_non_local(self) -> "Config":
        if self.ENVIRONMENT.is_deployed and not self.SENTRY_DSN:
            raise ValueError("Sentry is not set")

        return self

    @property
    def first_superuser(self):
        # Override FIRST_SUPERUSER for testing environment
        if self.ENVIRONMENT == Environment.TESTING:
            return "test@test.com"  # Default superuser for testing
        return self.FIRST_SUPERUSER

    @property
    def first_superuser_password(self):
        # Override FIRST_SUPERUSER_PASSWORD for testing environment
        if self.ENVIRONMENT == Environment.TESTING:
            return "testpassword"  # Default password for testing
        return self.FIRST_SUPERUSER_PASSWORD


settings = Config()  # type: ignore

app_configs: dict[str, Any] = {
    "title": "App API",
    "version": f"v{settings.APP_VERSION}",
}

app_configs["root_path"] = f"/api/v{settings.APP_VERSION}"

if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
