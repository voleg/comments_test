from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from comments_test.blog.models import Blog, Post
from comments_test.comment.models import Comment


class CommentsTestCases(APITestCase):

    def setUp(self):
        super().setUp()
        self.creator = User.objects.create_user(
            'test_user',
            email='test@example.com',
            password=None
        )
        # self.token = Token.objects.create(user=self.creator)
        self.blog = Blog.objects.create(name='test_blog', owner=self.creator, is_active=True)
        self.post = Post.objects.create(
            blog=self.blog,
            title='Comments Test Post',
            text='Lorem ipsum dolor sit amet ... '
        )
        self.client.force_authenticate(user=self.creator)

    def test_comment_creation(self):
        url = reverse('api:comment-list')
        data = {
            'title': 'test comment',
            'text': 'comment text',
            'object_type': 'blog.post',
            'object_id': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Comment.objects.count(), 1)
        self.assertTrue('comment_id' in response.data)

    def test_comment_editing(self):
        url = reverse('api:comment-list')
        data = {
            'title': 'test comment',
            'text': 'comment text',
        }
        response = self.client.put(url, data, format='json')

    def test_comment_delete(self):
        url = reverse('api:comment-list')
        pass
