from fastapi import APIRouter, HTTPException

from app.api.responses import BerryStatsResponse
from app.core.exceptions import ServiceError
from app.services.berry_service import berry_service

router = APIRouter(
    prefix="/v1",
    tags=["berry-stats"]
)


@router.get(
    "/allBerryStats",
    response_model=BerryStatsResponse,
    response_description="Berry Statistics",
    responses={
        200: {
            "description": "Statistics calculated successfully",
            "content": {
                "application/json": {
                    "example": BerryStatsResponse.Config.json_schema_extra["example"]
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "example": {"error": "Internal server error"}
                }
            }
        }
    }
)
async def get_berry_stats():
    """
    Asynchronously retrieves berry statistics.
    This function calls the BerryService to obtain statistics related to berries. 
    It handles potential service errors and raises an HTTPException with a 500 status code if an error occurs.

    Returns:
        The result of the berry statistics retrieval.

    Raises:
        HTTPException: If a ServiceError occurs or if an unexpected error arises during the process.
    """
    try:
        return await berry_service.get_all_berry_stats()
    except ServiceError as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
