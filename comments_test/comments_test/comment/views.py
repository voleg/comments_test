from rest_framework.viewsets import ViewSet
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from django.contrib.auth.models import User

from .models import Comment, CommentController
from .serializers import CommentSerializer

from rest_framework.authentication import TokenAuthentication


class CommentViewSet(ViewSet):
    queryset = Comment.objects.all()
    serializer = CommentSerializer
    controller = CommentController()

    def create(self, request):
        serializer = self.serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        content_object = data['content_object']

        if not request.user.is_authenticated():
            raise exceptions.PermissionDenied(detail='The user you specified is not exists')

        data['author'] = request.user

        if not content_object:
            raise exceptions.NotFound(detail='The object you specified is not found')

        comment = self.controller.create(**data)
        return Response({'comment_id': comment.pk}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        pass

    def list(self, request):
        return Response()

    def retrieve(self, request, pk=None):
        return Response()

    def destroy(self, request, pk=None):
        return Response()
