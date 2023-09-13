from pydantic import root_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @root_validator(skip_on_failure=True)
    def get_database_url(cls, values):
        values['DATABASE_URL'] = f'postgresql+asyncpg://{values["DB_USER"]}:{values["DB_PASSWORD"]}@{values["DB_HOST"]}:{values["DB_PORT"]}/{values["DB_NAME"]}'
        return values

    SECRET: str
    ALGORITHM: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
print(settings.DATABASE_URL)
print(settings.SECRET)
