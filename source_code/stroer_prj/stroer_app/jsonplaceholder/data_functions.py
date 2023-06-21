import requests

from stroer_app.utils.validate_response import validate_response
from stroer_app.db.dbpost import add_post as add_db_post
from stroer_app.db.dbcomment import add_comment as add_db_comment
from stroer_app.jsonplaceholder.enum import JsonPlaceHolder


def get_request() -> requests:
    """Get the connection with Post and Comment data of the JsonPlaceHolder.

    Returns
    -------
    Boolean
        Return the Post and Comment requests.
    """
    return requests.get(JsonPlaceHolder.POST_JPH_URL.value), requests.get(JsonPlaceHolder.COMMENTS_JPH_URL.value)


def jsonplaceholder_conection() -> bool:
    """Validate the connection with Post and Comment data of the JsonPlaceHolder.

    Returns
    -------
    Boolean
        Return True if the status response is HTTP 200 OK success.
    """
    posts_request, comment_request = get_request()
    if not (validate_response([posts_request, comment_request])):
        return False
    return True


def add_data() -> None:
    """Add Posts and Comments datas of the JsonPlaceHolder.
    """
    posts_request, comment_request = get_request()
    add_posts(posts_request.json())
    add_comments(comment_request.json())


def add_posts(posts_data) -> None:
    """Add Posts datas of the JsonPlaceHolder.

    Parameters
    ----------
    posts_data: json
        Json with the Posts datas.
    """
    for post_data in posts_data:
        add_post(post_data)


def add_comments(comments_data) -> None:
    """Add Comments datas of the JsonPlaceHolder.

    Parameters
    ----------
    comments_data: json
        Json with the Comments datas.
    """
    for comment_data in comments_data:
        add_comment(comment_data)


def add_post(post_data) -> None:
    """Add Post data of the JsonPlaceHolder.

    Parameters
    ----------
    post_data: array
        Array with a Post data.
    """
    add_db_post(
        post_data['userId'],
        post_data['title'],
        post_data['body'],
        JsonPlaceHolder.DATA_SOURCE.value,
        post_data['id']
    )


def add_comment(comment_data) -> None:
    """Add Comment data of the JsonPlaceHolder.

    Parameters
    ----------
    comment_data: array
        Array with a Comment data.
    """
    add_db_comment(
        comment_data['postId'],
        comment_data['name'],
        comment_data['email'],
        comment_data['body'],
        JsonPlaceHolder.DATA_SOURCE.value,
        comment_data['id']
    )
