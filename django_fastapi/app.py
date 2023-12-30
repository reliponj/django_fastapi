from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from django.conf import settings

from .asgi import application
from .routers import api_router


PROJECT_NAME = 'Django Fastapi'
API_PREFIX = '/api'
VERSION = '0.1.0'


fastapp = FastAPI(
    title=PROJECT_NAME,
    debug=settings.DEBUG,
    version=VERSION,
)

fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapp.include_router(api_router, prefix=API_PREFIX)

if settings.MOUNT_DJANGO_APP:
    fastapp.mount("/static", StaticFiles(directory=settings.STATIC_ROOT), name="static")
    fastapp.mount("/media", StaticFiles(directory=settings.MEDIA_ROOT), name="static")
    fastapp.mount("", application)
