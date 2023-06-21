from stroer_app.db.dbpost import get_exist_data_source_data
from stroer_app.jsonplaceholder.enum import JsonPlaceHolder


def exists_jsonplaceholder() -> bool:
    """Verify exists posts with data source equal JsonPlaceHolder.

    Returns
    -------
    Boolean
        Return True if exists posts with data source equal JsonPlaceHolder.
    """
    return get_exist_data_source_data(JsonPlaceHolder.DATA_SOURCE.value)
