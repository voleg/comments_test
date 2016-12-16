from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from rest_framework import exceptions
from treebeard.mp_tree import MP_Node

from comments_test.core.models import TimeStampableMixin

__all__ = ['Comment', 'CommentController', 'CommentableMixin']


class CommentableMixin(models.Model):
    enable_comments = models.BooleanField('Comments enabled', default=True)

    def comments_enabled(self):
        return self.enable_comments

    class Meta:
        abstract = True



class Comment(MP_Node, TimeStampableMixin):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='author', blank=False, db_index=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, db_index=True)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    node_order_by = ['created']

    def __str__(self):
        return 'Comment: {}'.format(self.title)


class Report(TimeStampableMixin, models.Model):
    STATUSES = (
        (0, 'new'),
        (1, 'running'),
        (2, 'ok'),
        (3, 'error')
    )
    owner = models.ForeignKey(User, related_name='reports')
    _file = models.FileField(upload_to='data/%Y/%m/%d')
    status = models.IntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return 'Report for {} #{}'.format(self.owner, self.pk)


class CommentController(object):

    def create(self, validated_data: dict):
        pass

    def update(self,
               instance: Comment,
               validated_data: dict):
        pass
