"""
Dependency injection for the Content Scraper API.

This module provides dependency injection functions for FastAPI.
"""

from services import ArticleService
from core.config import settings


def get_article_service() -> ArticleService:
    """
    Dependency provider for ArticleService.

    Returns:
        ArticleService: Configured article service instance
    """
    return ArticleService(
        language=settings.NEWSPAPER_LANGUAGE,
        user_agent=settings.NEWSPAPER_USER_AGENT,
    )
