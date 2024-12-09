from django.urls import path, include
from . import views
from .views import create_post
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create_post/', create_post, name='create_post'),
    path('accounts/', include('accounts.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('search/', views.search, name='search'),
]

if settings.DEBUG:  # Добавляем обработку медиафайлов в конце
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
