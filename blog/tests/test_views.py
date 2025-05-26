from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)

    def test_post_detail_view(self):
        """Перевіряє, що детальна сторінка поста доступна"""
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_create_post_authenticated(self):
        """Перевіряє, що авторизований користувач може створити пост"""
        response = self.client.post(reverse("create_post"), {"title": "New Post", "content": "Test content"})
        self.assertEqual(response.status_code, 302)  # Очікуваний редирект