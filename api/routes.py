"""
API routes for the Content Scraper API.

This module defines the API endpoints for the application.
"""

import logging
from fastapi import APIRouter, Depends, HTTPException, status
from api.models import ArticleRequest, ArticleResponse, ErrorResponse
from api.dependencies import get_article_service
from services import ArticleService, ArticleExtractionError


logger = logging.getLogger(__name__)

# Create router
router = APIRouter(prefix="", tags=["article"])


@router.post(
    "/fetch-article",
    response_model=ArticleResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse},
    },
    summary="Fetch and parse article content",
    description="Fetches an article from the provided URL and returns its structured content",
)
async def fetch_article(
    request: ArticleRequest,
    article_service: ArticleService = Depends(get_article_service),
) -> ArticleResponse:
    """
    Fetch and parse an article from the provided URL.

    Args:
        request: Request containing the article URL
        article_service: Injected article service

    Returns:
        Structured article content

    Raises:
        HTTPException: If article extraction fails
    """
    try:
        logger.info(
            "Received request to fetch article from URL: %s", request.url)

        # Extract article using the service
        article_data = article_service.extract_article(str(request.url))

        # Return the response
        return ArticleResponse(**article_data)

    except ArticleExtractionError as e:
        logger.error("Article extraction error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        ) from e  # Explicit chaining
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}",
        ) from e  # Explicit chaining
