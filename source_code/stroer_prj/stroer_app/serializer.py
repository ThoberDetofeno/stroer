from rest_framework import serializers

from stroer_app.models import Post
from stroer_app.models import Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'body']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['post_id', 'name', 'email', 'body']
