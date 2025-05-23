"""
API data models for the Content Scraper API.

This module contains Pydantic models for request and response validation.
"""

from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field


class ArticleRequest(BaseModel):
    """
    Request model for article fetching endpoint.
    """
    url: HttpUrl = Field(...,
                         description="URL of the article to fetch and parse")


class ArticleMetadata(BaseModel):
    """
    Model for additional article metadata.
    """
    publish_date: str = Field(
        default="", description="Publication date of the article")
    keywords: List[str] = Field(
        default=[], description="Keywords extracted from the article")
    summary: str = Field(default="", description="Summary of the article")
    meta_description: str = Field(
        default="", description="Meta description from HTML")
    meta_keywords: List[str] = Field(
        default=[], description="Keywords from meta tags")
    meta_lang: str = Field(default="", description="Language from meta tags")
    meta_favicon: str = Field(
        default="", description="Favicon URL from meta tags")
    canonical_link: str = Field(
        default="", description="Canonical link from meta tags")
    tags: List[str] = Field(
        default=[], description="Tags extracted from the article")
    source_url: str = Field(
        default="", description="Source URL of the article")


class ArticleResponse(BaseModel):
    """
    Response model for article content.
    """
    url: str = Field(..., description="Original URL of the article")
    title: str = Field(..., description="Title of the article")
    content: str = Field(..., description="Main text content of the article")
    top_image: Optional[str] = Field(
        None, description="URL of the top image in the article")
    authors: List[str] = Field(
        default=[], description="List of article authors")
    images: List[str] = Field(
        default=[], description="List of image URLs in the article")
    movies: List[str] = Field(
        default=[], description="List of video URLs in the article")
    additional_data: Optional[ArticleMetadata] = Field(
        default=None, description="Additional metadata about the article")


class ErrorResponse(BaseModel):
    """
    Response model for error messages.
    """
    detail: str = Field(..., description="Error message")
