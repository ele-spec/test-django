from django.test import TestCase
from blog.forms import PostForm

class PostFormTest(TestCase):
    def test_valid_form(self):
        """Перевіряє валідність правильно заповненої форми"""
        form_data = {"title": "Test Form", "content": "Testing content"}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Перевіряє, що порожня форма не є валідною"""
        form_data = {"title": "", "content": ""}
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

