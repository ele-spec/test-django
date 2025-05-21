from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_create_post(self):
        post = Post.objects.create(title="Test Post", content="Some content", author=self.user)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.author.username, "testuser")