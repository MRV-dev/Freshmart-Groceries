from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = "sqlite:///./employees.db"  # Use PostgreSQL in prod: "postgresql://user:password@localhost/dbname"
    ESB_URL: str = "http://esb-service-url"

settings = Settings()
