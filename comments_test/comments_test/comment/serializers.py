from rest_framework import serializers

from .models import CommentController


class CommentSerializer(serializers.Serializer, CommentController):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    author = serializers.CharField()

    object_type = serializers.CharField()
    object_id = serializers.IntegerField()
