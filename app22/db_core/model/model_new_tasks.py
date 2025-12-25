from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from app22.db_core.base import Base


class TaskOne(Base):
    __tablename__ = "task_one"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    msg = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())


class TaskTwo(Base):
    __tablename__ = "task_two"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String(255))
