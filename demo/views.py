from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from demo.forms import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from demo.models import *
from django.db.models import Q


# Home Page

class Home(View):

    def get(self, request):
        
        if not request.user.is_authenticated:
            return redirect('login')

        user = request.user

        return render(request, 'demo/home.html')

# SignUp Page

class SignUp(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'demo/signup.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, 'demo/signup.html', {'form' : form})



# Login Page

class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'demo/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return redirect('home')
        return render(request, 'demo/login.html', {'form': form})

# Create Video, Edit, Delete, List

class CreateVideo(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        form = VideoForm()
        return render(request, 'demo/create_video.html', {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
            
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                video = form.save(commit=False)
                video.user = request.user
                video.save()
                return redirect('home')
        else:
            form = VideoForm()
        return render(request, 'demo/create_video.html', {'form': form})   

class EditVideo(View):
    
    def get(self, request, video_id):
        if not request.user.is_authenticated:
            return redirect('login')

        video = Video.objects.get(id=video_id, user=request.user)
        form = VideoForm(instance=video)
        return render(request, 'demo/edit_video.html', {'form': form})

    def post(self, request, video_id):
        if not request.user.is_authenticated:
            return redirect('login')

        video = Video.objects.get(id=video_id, user=request.user)
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')
        return render(request, 'demo/edit_video.html', {'form': form})

class DeleteVideo(View):

    def get(self, request, video_id):
        if not request.user.is_authenticated:
            return redirect('login')

        video = Video.objects.get(id=video_id, user=request.user)
        return render(request, 'demo/delete_video.html', {'video': video})

    def post(self, request, video_id):
        if not request.user.is_authenticated:
            return redirect('login')

        video = Video.objects.get(id=video_id, user=request.user)
        video.delete()
        return redirect('video_list')

class VideoList(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        query = request.GET.get('q')
        videos = Video.objects.all()

        if query:
            videos = videos.filter(Q(name__icontains=query))

        return render(request, 'demo/video_list.html', {'videos': videos, 'query': query})



# Logout

class Logout(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            Token.objects.filter(user=request.user).delete()
            logout(request)
            return redirect('login')


