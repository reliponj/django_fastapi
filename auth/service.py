from auth.schemas import SignInSchema, AccessTokenSchema, SignUpSchema, RefreshSchema, OnlyAccessTokenSchema
from core.auth import password_service
from core.schemas import Response
from core.service import BaseService
from user.models import AppUser


class AuthService(BaseService):
    model = AppUser

    def sign_in(self, sign_in_data: SignInSchema):
        from core.jwt import jwt_service

        user = self.get(email=sign_in_data.email)
        if not user:
            return Response(status=False, message='user_not_found')

        if not password_service.verify_password(sign_in_data.password, user.password_hash):
            return Response(status=False, message='invalid_credentials')

        access_token = jwt_service.create_jwt_token(user, token_type='access')
        refresh_token = jwt_service.create_jwt_token(user, token_type='refresh')
        return AccessTokenSchema(access_token=access_token, refresh_token=refresh_token, user=user)

    def sign_up(self, sign_up_data: SignUpSchema):
        from core.jwt import jwt_service

        user = self.get(email=sign_up_data.email)
        if user:
            return Response(status=False, message='user_exists')

        user = AppUser(
            email=sign_up_data.email,
            password=sign_up_data.password)
        user.save()
        access_token = jwt_service.create_jwt_token(user, token_type='access')
        refresh_token = jwt_service.create_jwt_token(user, token_type='refresh')
        return AccessTokenSchema(access_token=access_token, refresh_token=refresh_token, user=user)

    def refresh(self, refresh_data: RefreshSchema):
        from core.jwt import jwt_service

        user = jwt_service.decode_jwt_token(refresh_data.refresh_token, token_type='refresh')
        access_token = jwt_service.create_jwt_token(user, token_type='access')
        return OnlyAccessTokenSchema(access_token=access_token, user=user)


auth_service = AuthService()
