from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import PostForm
from django.contrib import messages

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_list')  # Перенаправление на страницу списка постов
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
