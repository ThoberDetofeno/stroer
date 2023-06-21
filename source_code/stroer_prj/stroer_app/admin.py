from django.contrib import admin

from stroer_app.models import Post
from stroer_app.models import Comment
from stroer_app.utils.enum import Config


class PostAdm(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title', 'body', 'data_source', 'external_id')
    list_display_links = ('id', 'user_id', 'title', 'body', 'data_source', 'external_id')
    search_fields = ('user_id', 'title', 'body', 'data_source', 'external_id', )
    list_per_page = Config.NUMBER_ROW_PAGE.value


admin.site.register(Post, PostAdm)


class CommentAdm(admin.ModelAdmin):
    list_display = ('id', 'post_id', 'name', 'email', 'body', 'data_source', 'external_id')
    list_display_links = ('id', 'post_id', 'name', 'email', 'body', 'data_source', 'external_id')
    search_fields = ('name', 'email', 'data_source', 'external_id', )
    list_per_page = Config.NUMBER_ROW_PAGE.value


admin.site.register(Comment, CommentAdm)
