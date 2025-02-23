import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Configuration settings for the application.

    This class defines various settings for the API, including host, port, version, and other configurations
    related to the PokeAPI and caching. It also specifies the environment file to load settings from.

    Attributes:
        API_HOST (str): The host address for the API.
        API_PORT (int): The port number for the API.
        API_VERSION (str): The version of the API.
        DEBUG (bool): Flag to enable or disable debug mode.
        POKEAPI_BASE_URL (str): The base URL for the PokeAPI.
        POKEAPI_TIMEOUT (int): The timeout duration for PokeAPI requests.
        CACHE_ENABLED (bool): Flag to enable or disable caching.
        CACHE_TTL (int): Time-to-live for cached items in seconds.
        GRAPH_DPI (int): The DPI setting for generated graphs.
        GRAPH_FORMAT (str): The format for generated graphs.

    """
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")  # nosec B104
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    API_VERSION: str = os.getenv("API_VERSION", "v1")
    DEBUG: bool = bool(os.getenv("DEBUG", "False"))
    ENV: str = os.getenv("ENV", "development")

    POKEAPI_BASE_URL: str = os.getenv("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2")
    POKEAPI_TIMEOUT: int = int(os.getenv("POKEAPI_TIMEOUT", "30"))
    CACHE_ENABLED: bool = bool(os.getenv("CACHE_ENABLED", "False"))
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", "3600"))
    GRAPH_DPI: int = int(os.getenv("GRAPH_DPI", "300"))
    GRAPH_FORMAT: str = os.getenv("GRAPH_FORMAT", "png")

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Retrieve the application settings.

    This function returns an instance of the Settings class, which contains the configuration for the API.
    It utilizes caching to improve performance by storing the settings after the first retrieval.

    Returns:
        Settings: An instance of the Settings class containing the application's configuration.

    """

    return Settings()


settings = get_settings()
