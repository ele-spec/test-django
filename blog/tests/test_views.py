from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_post_detail(self):
        post = Post.objects.create(title="Test Post", content="Some content", author=self.user)
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")