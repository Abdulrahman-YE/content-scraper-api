# Content Scraper API

A high-performance FastAPI microservice that extracts content from web articles using newspaper3k, providing structured data through a RESTful API.

## Features

- **Article Extraction**: Extracts comprehensive article data including:
  - Title and main content
  - Authors and publication date
  - Images and videos
  - Meta information (keywords, description, language)
  - Additional metadata
- **Clean Architecture**: Modular design with clear separation of concerns
- **FastAPI Framework**: High performance, automatic OpenAPI documentation
- **Error Handling**: Robust error handling for various failure scenarios
- **Type Safety**: Full type hints and Pydantic models for request/response validation

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/content-scraper-api.git
cd content-scraper-api
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Starting the server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

### API Endpoints

#### POST /fetch-article

Fetches and parses an article from the provided URL.

**Request:**

```json
{
  "url": "https://example.com/news/article"
}
```

**Response:**

```json
{
  "url": "https://example.com/news/article",
  "title": "Example Article Title",
  "content": "Article content text...",
  "top_image": "https://example.com/images/top.jpg",
  "authors": ["Author Name"],
  "images": [
    "https://example.com/images/1.jpg",
    "https://example.com/images/2.jpg"
  ],
  "movies": ["https://example.com/videos/1.mp4"]
}
```

### API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Architecture

The application follows a clean architecture approach with the following components:

- **API Layer**: Handles HTTP requests and responses
- **Service Layer**: Contains the business logic for article extraction
- **Core**: Configuration and shared utilities

## Error Handling

The API handles various error scenarios:

- Invalid URLs
- Unreachable sites
- Parsing failures
- Server errors

## Extending the API

The modular architecture makes it easy to extend the API:

- Add new endpoints in `api/routes.py`
- Add new services in the `services` package
- Modify the data models in `api/models.py`

## License

MIT
