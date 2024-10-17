from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required  # Эта декоратор требует, чтобы пользователь был залогинен
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Устанавливаем автора поста
            post.save()
            return redirect('post_detail', pk=post.pk)  # Перенаправление на страницу поста
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

