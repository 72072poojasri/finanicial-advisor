from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories import UserRepository
from app.services import AuthService


def get_auth_service(
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)
    return AuthService(repository)