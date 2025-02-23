from typing import Dict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.v1 import router as v1_router
from app.core.config import settings
from app.core.exceptions import BaseAPIException

app = FastAPI(
    title="Poke Berry Stats API",
    description="API for getting statistics on Pokémon berries",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router)


@app.exception_handler(BaseAPIException)
async def api_exception_handler(request, exc: BaseAPIException) -> JSONResponse:
    """
    Handles exceptions of type BaseAPIException for the API.

    This asynchronous function is designed to catch and process exceptions that derive from BaseAPIException.
    It returns a JSON response containing the error message and the corresponding HTTP status code.

    Args:
        request: The incoming request that triggered the exception.
        exc (BaseAPIException): The exception instance that was raised.

    Returns:
        JSONResponse: A JSON response containing the error message and status code.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException) -> JSONResponse:
    """
    Handles HTTP exceptions for the API.

    This asynchronous function is designed to catch and process HTTPException instances.
    It returns a JSON response containing the error detail and the corresponding HTTP status code.

    Args:
        request: The incoming request that triggered the exception.
        exc (HTTPException): The exception instance that was raised.

    Returns:
        JSONResponse: A JSON response containing the error detail and status code.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception) -> JSONResponse:
    """
    Handles general exceptions for the API.

    This asynchronous function is designed to catch and process any unhandled exceptions that occur within the API.
    It returns a JSON response with a generic error message and a status code of 500, indicating an internal server error.

    Args:
        request: The incoming request that triggered the exception.
        exc (Exception): The exception instance that was raised.

    Returns:
        JSONResponse: A JSON response containing a generic error message and a status code of 500.
    """
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


@app.get("/", tags=["health"])
async def root() -> Dict[str, str]:
    """
    Root endpoint
    """
    return {
        "status": "ok",
        "message": "Poke Berry Stats API is running",
        "version": "1.0.0"
    }


@app.get("/health", tags=["health"])
async def health_check() -> Dict[str, str]:
    """
    Endpoint for health check
    """
    return {
        "status": "healthy",
        "service": "Poke Berry Stats API",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )
