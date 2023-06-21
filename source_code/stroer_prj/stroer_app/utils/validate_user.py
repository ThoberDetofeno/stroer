from stroer_app.utils.enum import UserPermition


def permission_new_post(user_id) -> bool:
    """Function validate if user has permissions to create new posts.

    The UserPermition class has the user codes with permissions to add new posts.

    Parameters
    ----------
    user_id : int
        Integer value that is user identification.

    Returns
    -------
    Boolean
        True is user has permitions.
    """
    return user_id in UserPermition.USER_ID_ALLOW.value
