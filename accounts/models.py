# accounts/models.py

from django.db import models
from django.contrib.auth.models import User
from blog.models import Post  # Импорт модели постов

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='accounts_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='accounts_comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
