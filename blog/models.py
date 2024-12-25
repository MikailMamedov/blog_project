from django.db import models
from django.contrib.auth.models import User
import random
from django.core.files.base import File
import os
from django.conf import settings 

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.image:  # Если изображения нет
            random_images = [
                'post_images/img1.jpg',
                'post_images/img2.jpg',
                'post_images/img3.jpg',
                'post_images/default.png',
            ]
            random_image_path = random.choice(random_images)
            absolute_path = os.path.join(settings.MEDIA_ROOT, random_image_path)

            if os.path.exists(absolute_path):  # Проверяем, что файл существует
                with open(absolute_path, 'rb') as f:
                    self.image.save(os.path.basename(random_image_path), File(f), save=False)
            else:
                print(f"Ошибка: файл {absolute_path} не найден.")
        
        super().save(*args, **kwargs)
        
    def get_image_url(self):
        if self.image and os.path.exists(self.image.path):
            return self.image.url
        return '/media/post_images/default.png'  # Путь должен начинаться с /media/


    def __str__(self):
        return self.title
