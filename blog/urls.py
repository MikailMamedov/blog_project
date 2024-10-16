from django.urls import path, include
from . import views
from .views import create_post
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.post_list, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('accounts/', include('accounts.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
