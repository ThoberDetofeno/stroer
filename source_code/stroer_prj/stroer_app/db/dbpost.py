from django.db.models import Max

from stroer_app.models import Post


def add_post(p_user_id, p_title, p_body, p_data_source, p_external_id):
    """Insert into Post table.

    Table: Post
    Columns: [user_id, title, body, data_source, external_id]

    Returns
    -------
    Object
        Return the Post instance.
    """
    return Post.objects.create(
        user_id=p_user_id,
        title=p_title,
        body=p_body,
        data_source=p_data_source,
        external_id=p_external_id)


def get_instance_by_external_id(p_data_source, p_external_id):
    """Return post instance by external id.

    Parameters
    ----------
    p_data_source : str
        Data source name.
    p_external_id : int
        Number of External ID.

    Returns
    -------
    Object
        Return the Post instance.
    """
    return Post.objects.get(external_id=p_external_id, data_source=p_data_source)


def get_exist_data_source_data(p_data_source) -> bool:
    """Return True if exists data in a data source.

    Parameters
    ----------
    p_data_source : str
        Data source name.
    """
    return Post.objects.filter(data_source=p_data_source).count() > 0


def del_post_by_data_source(p_data_source) -> None:
    """Delete all Post and Comments linked with a data source.

    Parameters
    ----------
    p_data_source : str
        Data source name.
    """
    Post.objects.filter(data_source=p_data_source).delete()


def get_exists_external_id(p_data_source, p_external_id) -> bool:
    """Verify if exists a external id of a data source.

    Parameters
    ----------
    p_data_source : str
        Data source name.
    p_external_id : int
        Number of External ID.

    Returns
    -------
    Boolean
        True if is has comment.
    """
    return Post.objects.filter(data_source=p_data_source, external_id=p_external_id).count() > 0


def get_max_external_id(p_data_source):
    """Return the Max external ID number.

    Parameters
    ----------
    p_data_source : str
        Data source name.

    Returns
    -------
    Decimal
        Max external ID number.
    """
    max_id = Post.objects.filter(data_source=p_data_source).aggregate(maxid=Max('external_id'))['maxid']
    return 0 if (max_id is None) else max_id
