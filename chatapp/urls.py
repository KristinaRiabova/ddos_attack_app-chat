from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
   path('login/', login_view, name='login_view'),
    path('registration/', views.registration_view, name='registration'),
    path('ddos/', views.ddos, name='ddos'),
    path('profile_created/', views.profile_created_view, name='profile_created'),
    path('profile/', views.read_profile, name='read_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('launch_attack/', views.launch_attack, name='launch_attack'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)