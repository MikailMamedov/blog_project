from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('profile/', views.profile, name='profile'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),

]