from typing import Self

from plateforme.resources import Auditable, BaseResource, CRUDResource, Field
from plateforme.api import AsyncSessionDep, Body, Id, route

from packages.users import User

from .utils import MediaType


class Tweet(CRUDResource, Auditable):
    """Tweet resource."""
    __config__ = {
        'endpoints': [('crud', {'include_method': 'GET'})],
    }

    owner: User = Field(association_alias='tweet_owner')
    content: str = Field(max_length=280)
    media: list['Media'] = Field(default_factory=list)

    mentions: list[User] = Field(default_factory=list, association_alias='tweet_mention', rel_load='selectin')
    hashtags: list['Hashtag'] = Field(default_factory=list, rel_load='selectin')

    original_tweet: 'Tweet | None' = Field(default=None, association_alias='tweet_retweet')
    is_retweet: bool = False
    parent_tweet: 'Tweet | None' = Field(default=None, association_alias='tweet_reply')
    is_reply: bool = False
    quoted_tweet: 'Tweet | None' = Field(default=None, association_alias='tweet_quote')
    is_quote: bool = False

    likes_count: int = 0
    retweets_count: int = 0
    replies_count: int = 0
    views_count: int = 0

    @route.post()
    @classmethod
    async def retweet(cls, session: AsyncSessionDep, owner_id: Id[User] = Body(), tweet_id: Id[Self] = Body()) -> Self:
        owner = await owner_id.resolve(session)
        tweet = await tweet_id.resolve(session)
        retweet = cls(
            owner=owner,
            content=tweet.content,
            original_tweet=tweet,
            is_retweet=True,
        )
        session.add(retweet)
        return retweet

    @route.post('')
    @classmethod
    async def create(cls, session: AsyncSessionDep, owner_id: Id[User] = Body(), content: str = Body()) -> Self:
        owner = await owner_id.resolve(session)
        tweet = cls(
            owner=owner,
            content=content,
        )
        session.add(tweet)
        return tweet


class Media(BaseResource):
    """Media resource."""
    url: str = ''
    media_type: MediaType = MediaType.IMAGE
    alt_text: str | None = None
    width: int = 0
    height: int = 0
    file_size: int = 0
    tweets: list[Tweet]


class Hashtag(BaseResource):
    """Hashtag resource."""
    name: str = Field(unique=True)
    tweet_count: int = 0
