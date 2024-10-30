"""app server module"""

from api.main import api_router
from core.config import settings
from core.db import initialize_db, mongo_lifespan
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware.middleware import RequestLoggingMiddleware


app = FastAPI(
    lifespan=mongo_lifespan,
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.on_event("startup")
def on_startup():
    initialize_db()
