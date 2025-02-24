from enum import StrEnum


class NotificationType(StrEnum):
    """Notification types."""
    LIKE = 'like'
    RETWEET = 'retweet'
    MENTION = 'mention'
    FOLLOW = 'follow'
    REPLY = 'reply'
    DIRECT_MESSAGE = 'direct_message'


class MediaType(StrEnum):
    """Media types."""
    IMAGE = 'image'
    VIDEO = 'video'
    GIF = 'gif'
