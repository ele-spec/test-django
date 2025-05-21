from blog.services import get_post
from unittest.mock import MagicMock, patch
from django.test import TestCase

class ServicesTest(TestCase):
    def test_mock_post(self):
        """Перевіряє підміну даних у функції get_post"""
        mock_post = MagicMock()
        mock_post.title = "Mocked Post"
        mock_post.content = "Mocked Content"

        get_post = MagicMock(return_value=mock_post)
        post = get_post()

        assert post.title == "Mocked Post"
        assert post.content == "Mocked Content"

    @patch("blog.models.Post.objects.get")
    def test_mock_get_post(self, mock_get):
        """Перевіряє, чи get_post повертає підмінний об'єкт"""
        mock_get.return_value.title = "Mocked Post"
        mock_get.return_value.content = "Mocked Content"

        post = get_post(post_id=1)

        assert post.title == "Mocked Post"
        assert post.content == "Mocked Content"

