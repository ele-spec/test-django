from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Profile, Post, Comment

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_profile_creation(self):
        """Перевіряє, чи профіль створюється правильно"""
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.user, self.user)

    def test_profile_str_method(self):
        """Перевіряє, чи `__str__` повертає правильне ім'я користувача"""
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(str(profile), "testuser")

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")

    def test_post_creation(self):
        """Перевіряє, чи пост створюється правильно"""
        post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "Test Content")
        self.assertEqual(post.author, self.user)

    def test_post_str_method(self):
        """Перевіряє, чи `__str__` повертає заголовок поста"""
        post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        self.assertEqual(str(post), "Test Post")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)

    def test_comment_creation(self):
        """Перевіряє, чи коментар створюється правильно"""
        comment = Comment.objects.create(post=self.post, user=self.user, content="Test Comment")
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.content, "Test Comment")

    def test_comment_str_method(self):
        """Перевіряє, чи `__str__` повертає правильний формат"""
        comment = Comment.objects.create(post=self.post, user=self.user, content="Test Comment")
        self.assertEqual(str(comment), "Comment by testuser on \"Test Post\"")
