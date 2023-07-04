"""Configuration Module."""

from dotenv import load_dotenv
from pydantic import BaseSettings, Field, SecretStr

load_dotenv()  # take environment variables from .env.


class DatabaseSettings(BaseSettings):
    db_salt: SecretStr = Field(..., env="DB_SALT")

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


DB_SETTINGS = DatabaseSettings()
