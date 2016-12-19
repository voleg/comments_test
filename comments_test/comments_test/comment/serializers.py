from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from .models import *


class CommentSerializer(serializers.Serializer):
    CONTENT_TYPE_SEP = '.'

    title = serializers.CharField(max_length=255)
    text = serializers.CharField()

    author = serializers.CharField(required=False)
    object_type = serializers.CharField()
    object_id = serializers.IntegerField()

    # will be dynamicly changed after validation
    content_object = serializers.Field(required=False)

    def validate_object_type(self, value):
        """
        :rtype: ContentType|None
        """
        app_label, _sep, model_name = value.partition(self.CONTENT_TYPE_SEP)
        if not all([app_label, model_name]):
            raise serializers.ValidationError('Please specify field in proper format')
        ct_obj_qs = ContentType.objects.filter(app_label=app_label, model=model_name)
        ct_obj = ct_obj_qs.first()
        return ct_obj

    def validate(self, data):
        data = super().validate(data)
        content_type = data['object_type']

        if content_type:
            data['content_object'] = content_type.get_all_objects_for_this_type(pk=data['object_id']).first()
        return data
