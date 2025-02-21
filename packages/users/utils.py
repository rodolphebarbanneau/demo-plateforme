from enum import Enum, auto


class UserRole(Enum):
    REGULAR = auto()
    VERIFIED = auto()
    ADMIN = auto()
