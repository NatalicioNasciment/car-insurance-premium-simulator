from pydantic_settings import BaseSettings



class Config(BaseSettings):
    ANNUAL_RATE: float
    RATE_PER_VALUE: float 
    BASE_VALUE: float

    class Config:
        env_file = ".env"

config = Config()
