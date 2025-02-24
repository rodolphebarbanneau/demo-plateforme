from enum import StrEnum


class UserRole(StrEnum):
    """User roles."""
    REGULAR = 'regular'
    VERIFIED = 'verified'
    ADMIN = 'admin'
