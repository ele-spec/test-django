import pytest
from django.contrib.auth.models import User
from blog.forms import UserRegisterForm, PostForm, CommentForm
from blog.models import Post, Comment

@pytest.mark.django_db
class TestUserRegisterForm:
    def test_user_register_form_valid_data(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        }
        form = UserRegisterForm(data=form_data)
        assert form.is_valid(), form.errors

    def test_user_register_form_invalid_passwords_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'WrongPass123!',
            'first_name': 'Test',
            'last_name': 'User',
        }
        form = UserRegisterForm(data=form_data)
        assert not form.is_valid()
        assert 'password2' in form.errors

    def test_user_register_form_duplicate_email(self):
        User.objects.create_user(username='existinguser', email='test@example.com', password='StrongPass123!')
        form_data = {
            'username': 'newuser',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        }
        form = UserRegisterForm(data=form_data)
        assert not form.is_valid()
        assert 'email' in form.errors
        assert form.errors['email'] == ["Користувач з такою адресою електронної пошти вже існує."]

    def test_user_register_form_save_commit_false(self):
        form_data = {
            'username': 'commituser',
            'email': 'commit@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        }
        form = UserRegisterForm(data=form_data)
        assert form.is_valid()
        user = form.save(commit=False)
        assert user.email == 'commit@example.com'
        assert user.pk is None  # Не збережено в базі

@pytest.mark.django_db
class TestPostForm:
    def test_post_form_valid_data(self):
        form_data = {'title': 'Test Post', 'content': 'This is test content'}
        form = PostForm(data=form_data)
        assert form.is_valid()

    def test_post_form_max_length_title(self):
        form_data = {'title': 'T' * 256, 'content': 'This is test content'}
        form = PostForm(data=form_data)
        assert not form.is_valid()
        assert 'title' in form.errors

@pytest.mark.django_db
class TestCommentForm:
    def test_comment_form_valid_data(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        post = Post.objects.create(title='Test Post', content='This is test content', author=user)  # ✅ Додано автора
        form_data = {'user': user, 'post': post, 'content': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        assert form.is_valid(), form.errors

    def test_comment_form_max_length_content(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        post = Post.objects.create(title='Test Post', content='This is test content', author=user)  # ✅ Додано автора
        form_data = {'user': user, 'post': post, 'content': 'T' * 1001}
        form = CommentForm(data=form_data)
        assert not form.is_valid()
        assert 'content' in form.errors
