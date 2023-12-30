from fastapi import APIRouter, Depends

from core.jwt import jwt_service
from user.models import AppUser
from user.schemas import UserSchema

user_router = APIRouter()


@user_router.get('/me/', summary='Profile', response_model=UserSchema)
def me(user: AppUser = Depends(jwt_service.get_active_user)):
    return user
