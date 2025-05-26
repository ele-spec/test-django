from django.urls import path
from .views import home, register, profile, create_post, post_detail

urlpatterns = [
    path('', home, name='home'),  # ✅ Головна сторінка
    path('register/', register, name='register'),  # ✅ Реєстрація
    path('profile/', profile, name='profile'),  # ✅ Профіль користувача
    path('post/new/', create_post, name='create_post'),  # ✅ Створення допису
    path('post/<int:pk>/', post_detail, name='post_detail'),  # ✅ Детальна сторінка поста
]