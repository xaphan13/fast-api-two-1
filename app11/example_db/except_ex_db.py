from fastapi.routing import APIRoute
from sqlalchemy.exc import IntegrityError
from typing import Callable
from fastapi import HTTPException, Request, Response


# app_fastapi = get_app_fastapi()
# @app_fastapi.exception_handler(IntegrityError)
# async def integrity_error_handler(request, exc):
#     body = await request.body()
#     detail = {"errors": exc.detail, "body": body.decode()}
#     raise HTTPException(status_code=422, detail=detail)


class MyApiRouter(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_route_handler(request)
            except IntegrityError as exc:
                if self.name == "add_user":
                    description = f"User уже существует - function={self.name}"
                elif self.name == "add_post":
                    description = f"Post уже существует - function={self.name}"
                else:
                    description = f"что то пошло не так - {self.name}"
                detail = {"errors": exc.__repr__(), "body": description}
                raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler
