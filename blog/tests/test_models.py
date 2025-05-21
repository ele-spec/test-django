from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(title="Test Post", content="Some content")
        self.assertEqual(post.title, "Test Post")
        self.assertTrue(post.created_on)

    def test_update_post(self):
        post = Post.objects.create(title="Old Title", content="Some content")
        post.title = "New Title"
        post.save()
        self.assertEqual(post.title, "New Title")

