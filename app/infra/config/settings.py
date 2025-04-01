from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ConfigDict



class Config(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")
    ANNUAL_RATE: float
    RATE_PER_VALUE: float 
    BASE_VALUE: float

config = Config()
