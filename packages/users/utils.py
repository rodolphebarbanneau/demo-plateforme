from enum import StrEnum


class UserRole(StrEnum):
    REGULAR = 'regular'
    VERIFIED = 'verified'
    ADMIN = 'admin'
