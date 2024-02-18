from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')


def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists():
          
            user = User.objects.create_user(username=username, password=password)
        
            login(request, user)
            return redirect('index')
        else:
            
            return render(request, 'registration.html', {'error_message': 'Username already exists'})
    else:
        return render(request, 'registration.html')


def ddos (request):

    return render(request, 'ddos.html')