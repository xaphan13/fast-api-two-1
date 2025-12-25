from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True


# class BaseBase:
#     id = Column(Integer, primary_key=True, index=True, unique=True)
# Base = declarative_base(cls=BaseBase)
