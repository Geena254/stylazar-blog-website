"""app server module"""

from api.main import api_router
from core.config import settings
from core.db import lifespan
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.request_logging import RequestLoggingMiddleware


app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://localhost:3000",
    "https://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)
