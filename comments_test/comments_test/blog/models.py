from django.db import models
from django.contrib.auth.models import User

from comments_test.comment.models import CommentableMixin


class Blog(models.Model):
    owner = models.ForeignKey(User, related_name='blog')
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(CommentableMixin, models.Model):
    blog = models.ForeignKey(Blog, related_name='posts')
    title = models.CharField(max_length=1024)
    text = models.TextField()

    def __str__(self):
        return self.title
