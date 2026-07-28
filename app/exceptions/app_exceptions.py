class UserAlreadyExistsException(Exception):
    """Raised when a user tries to register with an existing email."""
    pass


class InvalidCredentialsException(Exception):
    """Raised when login credentials are invalid."""
    pass


class UnauthorizedException(Exception):
    """Raised when a user is not authorized to access a resource."""
    pass


class ResourceNotFoundException(Exception):
    """Raised when a requested resource does not exist."""
    pass