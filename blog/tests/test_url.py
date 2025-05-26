from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import home, register, profile, create_post, post_detail

class UrlsTest(SimpleTestCase):
    def test_home_url(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_register_url(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func, register)

    def test_profile_url(self):
        url = reverse("profile")
        self.assertEqual(resolve(url).func, profile)

    def test_create_post_url(self):
        url = reverse("create_post")
        self.assertEqual(resolve(url).func, create_post)

    def test_post_detail_url(self):
        url = reverse("post_detail", args=[1])
        self.assertEqual(resolve(url).func, post_detail)