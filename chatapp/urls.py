from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('ddos/', views.ddos, name='ddos'),
    path('profile_created/', views.profile_created_view, name='profile_created'),
    path('profile/', views.read_profile, name='read_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('launch_attack/', views.launch_attack, name='launch_attack'),
]