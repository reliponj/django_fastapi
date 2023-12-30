from typing import Any, Union

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth.schemas import SignInSchema, AccessTokenSchema, SignUpSchema, RefreshSchema, OnlyAccessTokenSchema
from auth.service import auth_service
from core.jwt import jwt_service
from core.schemas import Response

token_router = APIRouter()
auth_router = APIRouter()


@token_router.post("/", summary="Login For Debug", response_model=Any)
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    sing_in_data = SignInSchema(
        email=form_data.username,
        password=form_data.password,
    )
    result = auth_service.sign_in(sing_in_data)
    if isinstance(result, Response):
        raise jwt_service.credentials_exception
    return {"access_token": result.access_token, "token_type": "bearer"}


@auth_router.post('/sign_in/', summary='Sign In', response_model=Union[Response, AccessTokenSchema])
def sign_in(sing_in_data: SignInSchema):
    return auth_service.sign_in(sing_in_data)


@auth_router.post('/sign_up/', summary='Sign Up', response_model=Union[Response, AccessTokenSchema])
def sign_up(sing_up_data: SignUpSchema):
    return auth_service.sign_up(sing_up_data)


@auth_router.post('/refresh/', summary='Refresh JWT', response_model=OnlyAccessTokenSchema)
def refresh(refresh_data: RefreshSchema):
    return auth_service.refresh(refresh_data)
