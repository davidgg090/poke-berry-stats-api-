from fastapi import APIRouter

from .endpoints.berry_stats import router as berry_stats_router

router = APIRouter()
router.include_router(berry_stats_router)
