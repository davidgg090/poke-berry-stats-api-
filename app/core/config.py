from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


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
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_VERSION: str = "v1"
    DEBUG: bool = False

    POKEAPI_BASE_URL: str = "https://pokeapi.co/api/v2"
    POKEAPI_TIMEOUT: int = 30


    CACHE_ENABLED: bool = False
    CACHE_TTL: int = 3600

    GRAPH_DPI: int = 300
    GRAPH_FORMAT: str = "png"

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
