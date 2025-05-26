from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']  # ✅ Оптимізовано: сортування постів від найновішого до найстарішого

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=1000)  # ✅ Додано обмеження довжини
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']  # ✅ Оптимізовано: коментарі сортуються від старіших до нових

    def __str__(self):
        return f'Comment by {self.user.username} on "{self.post.title}"'
