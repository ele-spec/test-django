from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostViewTest(TestCase):
    def setUp(self):
        """Створення тестового користувача перед кожним тестом"""
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_post_detail(self):
        """Перевіряє завантаження сторінки детального перегляду поста"""
        post = Post.objects.create(title="Test Post", content="Some content", author=self.user)
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_create_post(self):
        """Перевіряє створення нового поста через форму"""
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse('create_post'), {"title": "New Post", "content": "Test content"})
        self.assertEqual(response.status_code, 302)  # Очікується редирект після успішного створення
        self.assertTrue(Post.objects.filter(title="New Post").exists())