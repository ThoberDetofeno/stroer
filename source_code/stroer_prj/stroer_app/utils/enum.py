from enum import Enum


class Config(Enum):
    """General parameters used in stroer_app.

    NUMBER_ROW_PAGE: Number of row per page in the admin site.
    DEFAULT_USER: User default to add Post.
    DEFAULT_DATA_SOURCE: Data source default to add Post.
    """
    NUMBER_ROW_PAGE = 20
    DEFAULT_USER = 99999942
    DEFAULT_DATA_SOURCE = 'stroer'


class UserPermition(Enum):
    """Class with the permissions of users.

    USER_ID_ALLOW: List of users that has permission to add Post.
    """
    USER_ID_ALLOW = [99999942]
