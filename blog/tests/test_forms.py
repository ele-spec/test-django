from django.test import TestCase
from blog.forms import PostForm

class FormsTest(TestCase):
    def test_valid_form(self):
        form_data = {"title": "Valid Title", "content": "Valid Content"}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())