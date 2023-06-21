from enum import Enum


class JsonPlaceHolder(Enum):
    """General parameters used in the import of JsonPlaceHolder.

    POST_JPH_URL: URL to import the Posts data.
    COMMENTS_JPH_URL: URL to import the Comments data.
    DATA_SOURCE: Data source name of JsonPlaceHolder.
    """
    POST_JPH_URL = 'https://jsonplaceholder.typicode.com/posts'
    COMMENTS_JPH_URL = 'https://jsonplaceholder.typicode.com/comments'
    DATA_SOURCE = 'jsonplaceholder'
