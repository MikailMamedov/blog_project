from django.db import models
from django.contrib.auth.models import User
import random

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  
    def get_image_url(self):
        if self.image:
            return self.image.url
        random_images = [
            'static/random_images/img1.jpg',
            'static/random_images/img2.jpg',
            'static/random_images/img3.jpg',
        ]
        return random.choice(random_images)

    def __str__(self):
        return self.title