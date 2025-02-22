
from datetime import date, datetime

from plateforme.resources import Auditable, CRUDResource, Field
from plateforme.types import Email, SecretStr

from .utils import UserRole


class User(CRUDResource, Auditable):
    username: str = Field(unique=True, max_length=50)
    email: Email = Field(unique=True)
    password: str = Field(unique=True)
    role: str = Field(default='regular', init=False)
    # TODO: password: SecretStr = Field(unique=True)
    # TODO: role: UserRole = Field(default=UserRole.REGULAR, init=False)

    display_name: str | None = Field(default=None, max_length=200)
    bio: str | None = Field(default=None, max_length=500)
    profile_image: str | None = Field(default=None)
    header_image: str | None = Field(default=None)
    location: str | None = Field(default=None)
    website: str | None = Field(default=None)
    birth_date: date | None = Field(default=None)

    followers: set['User'] = Field(
        default_factory=set,
        association_alias='user_followers',
    )
    following: set['User'] = Field(
        default_factory=set,
        association_alias='user_following',
    )

    users_blocked: set['User'] = Field(
        default_factory=set,
        association_alias='user_blocked',
    )
    users_muted: set['User'] = Field(
        default_factory=set,
        association_alias='user_muted',
    )

    is_active: bool = Field(default=True, init=False)
    is_private: bool = Field(default=False, init=False)
    last_login: datetime | None = Field(default=None, init=False)

    tweet_count: int = Field(default=0, init=False)
    followers_count: int = Field(default=0, init=False)
    following_count: int = Field(default=0, init=False)
