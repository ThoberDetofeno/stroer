def validate_response(request_list) -> bool:
    """Function is to validate the status code of a request list.

    Parameters
    ----------
    request_list: list
        Request list.

    Returns
    -------
    Boolean
        Return True if all status code is HTTP 200 OK success.
    """
    for response in request_list:
        if response.status_code != 200:
            return False
    return True
