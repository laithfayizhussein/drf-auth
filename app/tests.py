from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class BlogTests(TestCase):

    @classmethod

    def setUpTest(cls):
        testuser = get_user_model().objects.create_user(username='admin', password='pass')
        testuser.save()
        testpost = Post.objects.create(title='Title', body='Hello World', author=testuser)
        testpost.save()
    
    def test_Blog(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'admin')
        self.assertEqual(expected_title, 'Title')
        self.assertEqual(expected_body, 'Hello World')