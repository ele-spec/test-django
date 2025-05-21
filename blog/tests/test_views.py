from django.test import TestCase
from django.urls import reverse
from blog.models import Post

class PostViewTest(TestCase):
    def test_post_detail(self):
        post = Post.objects.create(title="Test Post", content="Some content")
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_invalid_post_detail(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)
