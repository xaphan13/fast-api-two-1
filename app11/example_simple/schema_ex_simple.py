from pydantic import BaseModel
from enum import Enum


class SimpleReqSchema(BaseModel):
    amount: int = 1
    x: int = 2
    y: int = 3


class SimpleRespSchema(BaseModel):
    x: int
    y: int
    result: int


class ModelName(int, Enum):
    x = 1
    y = 2
