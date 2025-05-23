"""
Configuration settings for the Content Scraper API.

This module contains the configuration settings for the application,
loaded from environment variables with sensible defaults.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings loaded from environment variables for the Content Scraper API.

    Includes application metadata, server configuration, and options for the newspaper3k library.
    """

    # Application settings
    PROJECT_NAME: str = "Content Scraper API"
    PROJECT_DESCRIPTION: str = "API for extracting content from web articles"
    VERSION: str = "0.1.0"

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG_MODE: bool = True

    # Newspaper3k settings
    NEWSPAPER_LANGUAGE: str = "en"
    NEWSPAPER_USER_AGENT: str = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create a global settings object
settings = Settings()
