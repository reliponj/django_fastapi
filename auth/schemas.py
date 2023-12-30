from core.schemas import BaseSchema
from user.schemas import UserSchema


class SignUpSchema(BaseSchema):
    email: str
    password: str


class SignInSchema(BaseSchema):
    email: str
    password: str


class AccessTokenSchema(BaseSchema):
    access_token: str
    refresh_token: str
    user: UserSchema


class OnlyAccessTokenSchema(BaseSchema):
    access_token: str
    user: UserSchema


class RefreshSchema(BaseSchema):
    refresh_token: str
