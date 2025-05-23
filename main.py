#!/usr/bin/env python3
"""
Content Scraper API - Main Application Entry Point

This module serves as the entry point for the Content Scraper API microservice.
It initializes the FastAPI application and starts the uvicorn server.
"""

import logging
import uvicorn
from fastapi import FastAPI
from api.routes import router as api_router
from core.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured FastAPI application instance
    """
    application = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.VERSION,
    )

    # Include API routes
    application.include_router(api_router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    """
    Actions to perform on application startup.
    """
    logger.info("Starting Content Scraper API")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform on application shutdown.
    """
    logger.info("Shutting down Content Scraper API")


if __name__ == "__main__":
    logger.info("Starting uvicorn server at %s:%s",
                settings.HOST, settings.PORT)
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
    )
