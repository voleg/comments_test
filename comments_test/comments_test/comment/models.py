from datetime import datetime

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

    def get_instance(self,
                     app_label: str = 'comment',
                     content_type: str = 'comment',
                     object_id: int = None):
        """ Extract an entity """
        pass

    def create(self, content_object=None, object_type=None, object_id=None, **kwargs):
        instance = content_object or self.get_instance(
            content_type=object_type, object_id=object_id)

        return self.create_for(
            instance,
            kwargs.get('author'),
            kwargs.get('title'),
            kwargs.get('text')
        )

    def create_for(self,
                   instance: models.Model,
                   author: models.Model,
                   title: str,
                   text: str):
        """ Crete a comment for given instance """
        if isinstance(instance, Comment):
            obj = instance.add_child(
                content_object=instance,
                author=author,
                title=title,
                text=text
            )
        else:
            obj = Comment.add_root(
                content_object=instance,
                author=author,
                title=title,
                text=text
            )

        return obj

    def notify_subscribers(self):
        pass

    def edit_comment(self,
                     obj: Comment,
                     author: models.Model = None,
                     title: str = None,
                     text: str = None):
        """ Edit a comment """

        obj.author = author or obj.author
        obj.title = title or obj.title
        obj.text = text or obj.text
        obj.save()
        return obj

    def get_comments_for(self,
                         instance: models.Model,
                         level: int = None):
        """
        :param level: the depth of branch to retrieve, if None then all branch will be extracted
        :param instance: could be a comment or any comment enabled entity

        Retrieve a comments for given entity
        """
        if isinstance(instance, Comment):
            pass
        else:
            pass

    def dump(self,
             instance: models.Model,
             start: datetime = None,
             end: datetime = None):
        """
        create dump for given instance in given interval
        """
        # TODO create here delayed task
        pass
