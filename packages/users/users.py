
from datetime import date, datetime

from plateforme.resources import Auditable, CRUDResource, Field
from plateforme.types import Email, SecretStr

from .utils import UserRole


class User(CRUDResource, Auditable):
    username: str = Field(unique=True, max_length=50)
    email: Email = Field(unique=True)
    password: SecretStr = Field(unique=True)
    role: UserRole = Field(default=UserRole.REGULAR, init=False)

    display_name: str | None = Field(default=None, max_length=200)
    bio: str | None = Field(default=None, max_length=500)
    profile_image: str | None = None
    header_image: str | None = None
    location: str | None = None
    website: str | None = None
    birth_date: date | None = None

    followers: set['User'] = Field(default_factory=set, association_alias='user_followers', init=False)
    following: set['User'] = Field(default_factory=set, association_alias='user_following', init=False)

    users_blocked: set['User'] = Field(default_factory=set, association_alias='user_blocked', init=False)
    users_muted: set['User'] = Field(default_factory=set, association_alias='user_muted', init=False)

    is_active: bool = Field(default=True, init=False)
    is_private: bool = Field(default=False, init=False)
    last_login: datetime | None = Field(default=None, init=False)

    tweet_count: int = Field(default=0, init=False)
    followers_count: int = Field(default=0, init=False)
    following_count: int = Field(default=0, init=False)

    class Read:
        __include__ = [
            'username',
            'display_name',
            'bio',
            'profile_image',
            'header_image',
            'location',
            'website',
            'birth_date',
            'followers_count',
            'following_count',
            'is_active',
            'is_private',
            'created_at',
            'updated_at',
        ]
