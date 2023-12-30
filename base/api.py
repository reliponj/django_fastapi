from fastapi import APIRouter

from base.models import Setting
from base.schemas import SettingsSchema

base_router = APIRouter()


@base_router.get("/settings/", summary="Get settings", response_model=SettingsSchema)
def settings():
    return Setting.get_settings()
