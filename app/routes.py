from fastapi import APIRouter

from app.auth import login_routes, user_routes
from app.config import settings
from app.products import routes as product_routes

api_router = APIRouter()

api_router.include_router(user_routes.router)
api_router.include_router(login_routes.router)
api_router.include_router(product_routes.router)


@api_router.get("/", include_in_schema=False)
async def main() -> dict[str, str]:
    return {
        "message": "API is running and avaible for use",
        "version": settings.APP_VERSION,
    }


@api_router.get("/health", include_in_schema=False)
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
