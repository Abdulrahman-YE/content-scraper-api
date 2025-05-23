"""
Article extraction service using newspaper3k.

This module provides services for downloading and parsing web articles.
"""

import logging
from typing import Dict, Any, List, Optional
from newspaper import Article, ArticleException
from core.config import settings

logger = logging.getLogger(__name__)


class ArticleExtractionError(Exception):
    """
    Exception raised when article extraction fails.
    """


class ArticleService:
    """
    Service for extracting content from web articles using newspaper3k.
    """

    def __init__(self, language: str = None, user_agent: str = None):
        """
        Initialize the article service with configuration.

        Args:
            language: Language for article parsing (default from settings)
            user_agent: User agent for HTTP requests (default from settings)
        """
        self.language = language or settings.NEWSPAPER_LANGUAGE
        self.user_agent = user_agent or settings.NEWSPAPER_USER_AGENT
        logger.info("Initialized ArticleService with language=%s",
                    self.language)

    def extract_article(self, url: str) -> Dict[str, Any]:
        """
        Download and extract content from the given URL.

        Args:
            url: URL of the article to extract

        Returns:
            Dict containing extracted article data

        Raises:
            ArticleExtractionError: If extraction fails
        """
        try:
            logger.info("Extracting article from URL: %s", url)

            # Initialize article
            article = Article(url, language=self.language)
            article.config.browser_user_agent = self.user_agent

            # Download and parse
            article.download()
            article.parse()

            # Extract and return data
            return self._format_article_data(article, url)

        except ArticleException as e:
            logger.error("Newspaper3k error: %s", e)
            raise ArticleExtractionError(
                f"Failed to extract article: {e}") from e
        except Exception as e:
            logger.error("Unexpected error during article extraction: %s", e)
            raise ArticleExtractionError(f"Unexpected error: {e}") from e

    def _format_article_data(self, article: Article, original_url: str) -> Dict[str, Any]:
        """
        Format the extracted article data into the response structure.

        Args:
            article: Parsed newspaper Article object
            original_url: Original URL requested

        Returns:
            Dict with formatted article data
        """
        # Get top image or None if not available
        top_image: Optional[str] = article.top_image if article.top_image else None

        # Get all images or empty list if none
        images: List[str] = list(article.images) if article.images else []

        # Get all videos or empty list if none
        movies: List[str] = article.movies if article.movies else []

        # Get authors or empty list if none
        authors: List[str] = article.authors if article.authors else []

        # Create response with required fields
        response = {
            "url": original_url,
            "title": article.title or "",
            "content": article.text or "",
            "top_image": top_image,
            "authors": authors,
            "images": images,
            "movies": movies
        }

        # Add additional metadata fields that might be useful for clients
        additional_data = {
            "publish_date": article.publish_date.isoformat() if article.publish_date else "",
            "keywords": article.keywords,
            "summary": article.summary,
            "meta_description": article.meta_description,
            "meta_keywords": article.meta_keywords,
            "meta_lang": article.meta_lang,
            "meta_favicon": article.meta_favicon,
            "canonical_link": article.canonical_link,
            "tags": list(article.tags) if article.tags else [],
            "source_url": article.source_url
        }

        # Store additional data in a separate field to keep the main response clean
        response["additional_data"] = additional_data

        return response
