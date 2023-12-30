from fastapi import APIRouter

from auth.api import auth_router, token_router
from base.api import base_router
from user.api import user_router

api_router = APIRouter()

api_router.include_router(token_router, prefix='/token', tags=['token'])
api_router.include_router(auth_router, prefix='/auth', tags=['auth'])
api_router.include_router(base_router, prefix='/base', tags=['base'])
api_router.include_router(user_router, prefix='/user', tags=['user'])
