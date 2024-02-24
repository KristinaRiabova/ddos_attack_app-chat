
from django.urls import path
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
]
