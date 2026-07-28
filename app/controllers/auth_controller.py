from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies.auth import get_auth_service
from app.schemas import (
    TokenResponse,
    UserRegister,
    UserResponse,
)
from app.services import AuthService


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: UserRegister,
    service: AuthService = Depends(get_auth_service),
):
    return service.register(
        request.email,
        request.password,
    )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
):
    return service.login(
        form_data.username,
        form_data.password,
    )