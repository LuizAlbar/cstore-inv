from pydantic_settings import BaseSettings

class Setting(BaseSettings):

    DATABASE_URL: str = 'postgresql+psycopg2://postgres:postgres@localhost:5432/cstore'

settings = Setting()