from fastapi.routing import APIRoute
from sqlalchemy.exc import NotSupportedError
from typing import Callable
from fastapi import HTTPException, Request, Response


class MyApiRouterMany(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except NotSupportedError as exc:
                if self.name == "add_user":
                    description = f"User уже существует - function={self.name}"
                elif self.name == "add_post":
                    description = f"Post уже существует - function={self.name}"
                else:
                    description = f"что то пошло не так - {self.name}"
                detail = {"errors": exc.__repr__(), "body": description}
                raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler
