from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.exceptions import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
)
from app.repositories import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(
        self,
        email: str,
        password: str,
    ):
        existing_user = self.repository.get_by_email(email)

        if existing_user:
            raise UserAlreadyExistsException(
                "Email already registered"
            )

        password_hash = hash_password(password)

        return self.repository.create(
            email=email,
            password_hash=password_hash,
        )

    def login(
        self,
        email: str,
        password: str,
    ):
        user = self.repository.get_by_email(email)

        if not user:
            raise InvalidCredentialsException(
                "Invalid email or password"
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise InvalidCredentialsException(
                "Invalid email or password"
            )

        token = create_access_token(user.id)

        return {
            "access_token": token,
            "token_type": "bearer",
        }