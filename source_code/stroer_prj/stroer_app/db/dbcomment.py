from django.db.models import Max

from stroer_app.models import Comment
from stroer_app.db.dbpost import get_instance_by_external_id as post_instance


def add_comment(p_post_id, p_name, p_email, p_body, p_data_source, p_external_id):
    """Insert into Comment table.

    Table: Comment
    Columns: [post_id, name, email, body, data_source, external_id]

    Returns
    -------
    Object
        Return the Comment instance.
    """
    return Comment.objects.create(
        post_id=post_instance(p_data_source, p_post_id),
        name=p_name,
        email=p_email,
        body=p_body,
        data_source=p_data_source,
        external_id=p_external_id)


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
    return Comment.objects.filter(data_source=p_data_source, external_id=p_external_id).count() > 0


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
    max_id = Comment.objects.filter(data_source=p_data_source).aggregate(maxid=Max('external_id'))['maxid']
    return 0 if (max_id is None) else max_id
