from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions import (
    InvalidCredentialsException,
    ResourceNotFoundException,
    UnauthorizedException,
    UserAlreadyExistsException,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(UserAlreadyExistsException)
    async def user_exists_exception_handler(
        request: Request,
        exc: UserAlreadyExistsException,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(InvalidCredentialsException)
    async def invalid_credentials_exception_handler(
        request: Request,
        exc: InvalidCredentialsException,
    ):
        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(ResourceNotFoundException)
    async def resource_not_found_exception_handler(
        request: Request,
        exc: ResourceNotFoundException,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(UnauthorizedException)
    async def unauthorized_exception_handler(
        request: Request,
        exc: UnauthorizedException,
    ):
        return JSONResponse(
            status_code=403,
            content={
                "success": False,
                "message": str(exc),
            },
        )