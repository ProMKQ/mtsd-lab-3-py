from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'spaceship'
    app_description: str = 'Laboratory assignment #3 starter project for software engineering course'
    app_version: str = 'dev'
    debug: bool = False
