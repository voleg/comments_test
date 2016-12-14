from django.db import models
from treebeard.mp_tree import MP_Node
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


__all__ = ['Comment']


class TimeStampableMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(MP_Node, TimeStampableMixin):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='author', blank=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    node_order_by = ['created']

    def __str__(self):
        return 'Comment: {}'.format(self.title)


class CommentController(object):

    def create(self, validated_data: dict):
        pass

    def update(self,
               instance: Comment,
               validated_data: dict):
        pass
