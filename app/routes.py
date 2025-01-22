from fastapi import APIRouter

from app.auth import login_routes, user_routes
from app.products import routes as product_routes

api_router = APIRouter()

api_router.include_router(user_routes.router)
api_router.include_router(login_routes.router)
api_router.include_router(product_routes.router)
