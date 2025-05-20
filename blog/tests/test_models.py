from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.post = Post.objects.create(title="Test Title", content="Test Content", author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.content, "Test Content")
        self.assertEqual(self.post.author.username, "testuser")