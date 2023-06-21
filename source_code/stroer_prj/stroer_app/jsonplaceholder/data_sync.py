from stroer_app.jsonplaceholder.data_functions import jsonplaceholder_conection
from stroer_app.jsonplaceholder.enum import JsonPlaceHolder
from stroer_app.jsonplaceholder.data_delete import delete_jsonplaceholder
from stroer_app.jsonplaceholder.data_import import import_jsonplaceholder
from stroer_app.jsonplaceholder.data_functions import get_request
from stroer_app.db.dbpost import get_exists_external_id as exists_post_id
from stroer_app.db.dbpost import get_max_external_id as last_post_id
from stroer_app.db.dbcomment import get_exists_external_id as exists_comment_id
from stroer_app.db.dbcomment import get_max_external_id as last_comment_id
from stroer_app.jsonplaceholder.data_functions import add_post
from stroer_app.jsonplaceholder.data_functions import add_comment


def forced_sync() -> bool:
    """Synchronization with JsonPlaceHolder - Option: forced.

    Delete all Posts and Comments and re-include.
    This option does not keep changed Post data and new comments on JsonPlaceHolder Posts.
    """
    delete_jsonplaceholder()
    return import_jsonplaceholder()


def add_sync() -> bool:
    """Synchronization with JsonPlaceHolder - Option: add.

    It includes all the Posts and Comments that are in JsonPlaceHolder but not in MASTER.
    This option retains changes made to the MASTER in JsonPlaceHolder Posts or Comments.
    """
    if not (jsonplaceholder_conection()):
        return False
    posts_request, comment_request = get_request()
    # Add all Posts that have in JsonPlaceHolder and do not have in MASTER.
    for post_data in posts_request.json():
        if not (exists_post_id(JsonPlaceHolder.DATA_SOURCE.value, post_data['id'])):
            add_post(post_data)
    # Add all Comments that have in JsonPlaceHolder and do not have in MASTER.
    for comment_data in comment_request.json():
        if not (exists_comment_id(JsonPlaceHolder.DATA_SOURCE.value, comment_data['id'])):
            add_comment(comment_data)
    return True


def check_sync() -> bool:
    """Synchronization with JsonPlaceHolder - Option: check.

    This option includes new posts and comments made after the last import.
    """
    posts_request, comment_request = get_request()
    # Add all Posts after the last import and do not have in MASTER
    for post_data in posts_request.json():
        if post_data['id'] > last_post_id(JsonPlaceHolder.DATA_SOURCE.value):
            add_post(post_data)
    # Add all Comments after the last import and do not have in MASTER.
    for comment_data in comment_request.json():
        if comment_data['id'] > last_comment_id(JsonPlaceHolder.DATA_SOURCE.value):
            add_comment(comment_data)
    return True
