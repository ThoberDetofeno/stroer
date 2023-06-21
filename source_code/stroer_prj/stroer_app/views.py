from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from stroer_app.models import Post
from stroer_app.models import Comment
from stroer_app.serializer import PostSerializer
from stroer_app.serializer import CommentSerializer
from stroer_app.utils.validate_user import permission_new_post


class PostViewSet(viewsets.ModelViewSet):
    """Rest API to manage that Post data.

    It were implement all CRUD operations to Post model.

    Example:
    --------------------------------------
    [POST] .../post/
        json: {
                "title": "laboriosam dolor",
                "body": "facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores"
              }
    [GET] .../post/
    [GET] .../post/1/
    [PUT] .../post/1/
        json: {
                "title": "new title",
                "body": "new body"
              }
    [DELETE] .../post/1/
    """
    http_method_names = ["post", "get", "put", "delete"]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'user_id']
    search_fields = ['user_id', 'title', 'body']
    filterset_fields = ['user_id', 'title', 'body']

    def update(self, request, *args, **kwargs):
        """Enable the partial update and not allow updating in user id.
        """
        if request.method == 'PUT' and 'user_id' in request.data:
            return Response({'user_id': 'Is not allow changing the user id!'}, status=status.HTTP_400_BAD_REQUEST)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Validate the user id in POST method.
        """
        if request.method == 'POST':
            if 'user_id' in request.data:
                user_id = request.data.get('user_id')  # type: ignore
                if not (user_id.isdigit()):
                    return Response({'user_id': 'The user is not an integer value!'}, status=status.HTTP_400_BAD_REQUEST)
                if not (permission_new_post(int(user_id))):
                    return Response({'user_id': 'The user is not permission to new post!'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommentViewSet(viewsets.ModelViewSet):
    """Rest API to manage that Comment data.

    It were implement all CRUD operations to Post model.

    Example:
    --------------------------------------
    [POST] .../comment/
        json: {
                "post_id": 101,
                "name": "et fugit eligendi deleniti quidem qui sint nihil autem",
                "email": "Presley.Mueller@myrl.com",
                "body": "doloribus at sed quis culpa deserunt consectetur qui praesentium"
              }
    [GET] .../comment/
    [GET] .../comment/1/
    [PUT] .../comment/1/
        json: {
                "post_id": 1,
                "name": "new name",
                "email": "new.email@myrl.com",
                "body": "newbody"
               }
    [DELETE] .../comment/1/
    """
    http_method_names = ["post", "get", "put", "delete"]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['id', 'postId']
    search_fields = ['post_id', 'name', 'email', 'body']
    filterset_fields = ['post_id', 'name', 'email', 'body']

    def update(self, request, *args, **kwargs):
        """Enable the partial update.
        """
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
