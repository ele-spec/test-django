from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, PostForm, CommentForm
from .models import Post, Comment, Profile

def home(request):
    """Відображає головну сторінку з дописами."""
    posts = Post.objects.order_by('-created_on')
    return render(request, 'blog/home.html', {'posts': posts})

def register(request):
    """Обробляє реєстрацію користувача."""
    form = UserRegisterForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Реєстрація пройшла успішно. Ви можете увійти.')
        return redirect('login')
    return render(request, 'blog/register.html', {'form': form})

@login_required
def create_post(request):
    """Обробляє створення нового допису."""
    form = PostForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, 'Ваш допис успішно створено!')
        return redirect('home')
    return render(request, 'blog/post_form.html', {'form': form})

def post_detail(request, pk):
    """Відображає детальну сторінку допису та дозволяє залишати коментарі."""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.order_by('created_on')
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Будь ласка, увійдіть, щоб залишити коментар.')
            return redirect('login')

        if form.is_valid():
            Comment.objects.create(user=request.user, post=post, **form.cleaned_data)
            messages.success(request, 'Ваш коментар успішно додано!')
            return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def profile(request):
    """Відображає профіль користувача та його дописи."""
    profile, _ = Profile.objects.get_or_create(user=request.user)
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/profile.html', {'profile': profile, 'posts': posts})