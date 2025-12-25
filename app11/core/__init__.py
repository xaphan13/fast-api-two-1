from fastapi import FastAPI
from app11.core.config import OPEN_API_PREFIX


app_fastapi = FastAPI(root_path=OPEN_API_PREFIX)


def get_app_fastapi():
    """получение экземпляра FastAPI"""
    return app_fastapi
