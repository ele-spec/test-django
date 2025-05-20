from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/new/', views.create_post, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
