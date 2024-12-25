import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm, CommentForm
from blog.models import Post
from django.contrib.auth.models import User

# Получение случайного изображения с Unsplash
def get_random_image():
    access_key = 'v9dXCi8I5vqQdYBk6yZAFPhCDvcA-vZkK3VH2wPTYtM'  # Ваш ключ API Unsplash
    url = f'https://api.unsplash.com/photos/random?client_id={access_key}&w=300&h=200'
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]['urls']['small']
    return None

# Страница со списком постов
def post_list(request):
    posts = Post.objects.all()

    # Для каждого поста, если у него нет изображения, добавить случайное
    for post in posts:
        if not post.image:
            random_image_url = get_random_image()
            if random_image_url:
                # Если нужно, можно сохранить картинку на сервере, но пока просто используем ссылку
                post.image = random_image_url
                post.save()

    return render(request, 'blog/index.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались! Теперь вы можете войти.')
            return redirect('login')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки ниже.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/profile.html')

# Страница с постом и комментариями
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Получаем пост по id
    comments = post.accounts_comments.all()  # Получаем все комментарии для этого поста
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Привязываем комментарий к посту
            comment.user = request.user  # Устанавливаем текущего пользователя как автора
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Перенаправляем на страницу этого поста
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    return render(request, 'accounts/profile.html', {'user': user, 'posts': posts})