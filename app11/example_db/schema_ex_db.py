from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# schemas are used when UPDATE column=version_num in row=1 in tables(alembic)
class MigrationUpdateBody(BaseModel):
    new_version: str  # Новый ID ревизии


class MigrationUpdateResponse(BaseModel):
    message: str
    new_version: str


# schemas are used when creating(.post) a User(Base) or Post(Base)
class UserCreateBody(BaseModel):
    nickname: str
    email: str
    firstname: Optional[str] = ""
    surname: Optional[str] = ""
    password: str


class PostCreateBody(BaseModel):
    title: str
    content: str


# schemas are used when updating(.update) a User(Base) or Post(Base)
class UserUpdateBody(BaseModel):
    nickname: Optional[str] = ""
    email: Optional[str] = ""
    firstname: Optional[str] = ""
    surname: Optional[str] = ""
    password: Optional[str] = ""


class PostUpdateBody(BaseModel):
    id: int
    title: Optional[str] = ""
    content: Optional[str] = ""


# schemas are used when searching(.get) for User(Base) or Post(Base)
class GetUserQuery(BaseModel):
    id: Optional[int] = None
    nickname: Optional[str] = None
    email: Optional[str] = None


class PostsOrderQuery(str, Enum):
    id = "id"
    time = "time"
    title = "title"
    user_id = "user_id"


class GetPostQuery(BaseModel):
    id: Optional[int] = None
    time_created: Optional[datetime] = None
    title: Optional[str] = None
    content: Optional[str] = None
    user_id: Optional[int] = None


# schema is used as a response_model for User(Base)
class UserPostBase(BaseModel):
    class Config:
        from_attributes = True


class UserSchemaResp(UserPostBase):
    id: int
    nickname: str
    email: str
    firstname: str
    surname: str


# schema is used as a response_model for Post(Base)
class PostSchemaResp(UserPostBase):
    id: int
    time_created: datetime
    title: str
    content: str
    user_id: int


# schema is used as a response_model for User(Base) -> added posts = relationship('Post'
class UserSchemaPostsResp(UserSchemaResp):
    posts: List[PostSchemaResp]


# schema is used as a response_model for Post(Base) -> added author = relationship('User'
class PostSchemaAuthorResp(PostSchemaResp):
    author: UserSchemaResp
