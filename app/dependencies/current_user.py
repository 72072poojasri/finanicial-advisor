from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import verify_access_token
from app.database.database import get_db
from app.exceptions import (
    InvalidCredentialsException,
    ResourceNotFoundException,
)
from app.repositories import UserRepository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = verify_access_token(token)

    if payload is None:
        raise InvalidCredentialsException(
            "Invalid or expired token"
        )

    user_id = int(payload["sub"])

    repository = UserRepository(db)

    user = repository.get_by_id(user_id)

    if user is None:
        raise ResourceNotFoundException(
            "User not found"
        )

    return user