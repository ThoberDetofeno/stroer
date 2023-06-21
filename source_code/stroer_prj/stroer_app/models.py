from django.db import models
from stroer_app.utils.enum import Config


class Post(models.Model):
    """Table with content created and published on any internet platform.

    Table: Post
    Columns:
        user_id: User identification
        title: Title of post
        body: Content of post
        data_source: Data source define the data origin.
        external_id: External id
    """
    user_id = models.DecimalField(max_digits=20, decimal_places=0, null=False, blank=False, default=Config.DEFAULT_USER.value)
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    data_source = models.CharField(max_length=255, null=False, blank=False, default=Config.DEFAULT_DATA_SOURCE.value)
    external_id = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)

    def __str__(self) -> str:
        return '{}'.format(self.title)


class Comment(models.Model):
    """Table with comments created and published in the Posts.

    Table: Comment
    Columns:
        post_id: Internal ID of a Post
        name: Name of user that do the post
        email: Email of contact
        body: Comment of a post
        data_source: Data source define the data origin.
        external_id: External id
    """
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, to_field='id', related_name='posts', blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    body = models.TextField(blank=False, null=False)
    data_source = models.CharField(max_length=255, null=False, blank=False, default=Config.DEFAULT_DATA_SOURCE.value)
    external_id = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)

    def __str__(self) -> str:
        return '[{}] {}'.format(self.name, self.body)
