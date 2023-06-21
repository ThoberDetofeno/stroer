from stroer_app.jsonplaceholder.data_exists import exists_jsonplaceholder
from stroer_app.jsonplaceholder.data_functions import add_data
from stroer_app.jsonplaceholder.data_functions import jsonplaceholder_conection


def import_jsonplaceholder() -> bool:
    """Import JSONPlaceholder datas.

    Returns
    -------
    Boolean
        Return True if import JSONPlaceholder had successy.
    """
    if exists_jsonplaceholder():
        return False
    if not (jsonplaceholder_conection()):
        return False
    add_data()
    return True
