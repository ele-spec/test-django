from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class PostModelTest(TestCase):
    def setUp(self):
        """Створення тестового користувача перед кожним тестом"""
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_create_post(self):
        """Перевіряє коректність створення поста"""
        post = Post.objects.create(title="Test Post", content="Some content", author=self.user)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.author.username, "testuser")
        self.assertIsNotNone(post.created_on)  # Перевіряє наявність дати створення

    def test_update_post(self):
        """Перевіряє оновлення поста"""
        post = Post.objects.create(title="Old Title", content="Some content", author=self.user)
        post.title = "New Title"
        post.save()
        self.assertEqual(post.title, "New Title")

    def test_post_str_method(self):
        """Перевіряє метод __str__ моделі Post"""
        post = Post.objects.create(title="Test Post", content="Some content", author=self.user)
        self.assertEqual(str(post), "Test Post")