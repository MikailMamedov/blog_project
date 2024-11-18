from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CommentForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .models import Comment
from blog.models import Post

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful.')
#             return redirect('index')
#         else:
#             messages.error(request, 'Registration failed. Please correct the errors.')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})

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
