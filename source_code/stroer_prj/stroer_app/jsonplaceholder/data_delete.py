from stroer_app.jsonplaceholder.enum import JsonPlaceHolder
from stroer_app.db.dbpost import del_post_by_data_source


def delete_jsonplaceholder() -> bool:
    """Delete all Post and Comments linked with JsonPlaceHolder data source.

    Returns
    -------
    Boolean
        Return True after the delete.
    """
    del_post_by_data_source(JsonPlaceHolder.DATA_SOURCE.value)
    return True
