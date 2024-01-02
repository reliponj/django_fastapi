from datetime import datetime, timedelta

from django.utils import timezone
from django.utils.timezone import make_aware
from fastapi import HTTPException, Depends
import jwt
from django.conf import settings
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from auth.service import auth_service
from user.models import AppUser


class JWTService:
    SECRET_KEY = settings.SECRET_KEY
    ALGORITHM = "HS256"
    EXPIRATIONS = {
        "access": 60 * 60,  # 1h
        "refresh": 60 * 60 * 24 * 7,  # 7d
    }
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token/")

    def create_jwt_token(self, user: AppUser, token_type: str = 'access'):
        expire = timezone.now() + timedelta(seconds=self.EXPIRATIONS[token_type])
        data = {
            "type": token_type,
            "id": str(user.id),
            "exp": expire,
        }
        return jwt.encode(data, self.SECRET_KEY, algorithm=self.ALGORITHM)

    def decode_jwt_token(self, token, token_type: str = None):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            id = payload.get("id")
            exp = payload.get("exp")
            type = payload.get("type")
            if token_type != type:
                raise self.credentials_exception

            date = make_aware(datetime.fromtimestamp(exp))
            user = auth_service.get(id=id)

            if date < timezone.now() or not user:
                raise self.credentials_exception
        except:
            raise self.credentials_exception
        return user

    def get_active_user(self, token: str = Depends(oauth2_scheme)):
        user = self.decode_jwt_token(token, token_type="access")
        return user


jwt_service = JWTService()
