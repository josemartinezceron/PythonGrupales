from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import IntegrityError
# Create your views here.
def home(request):
    return render(request, 'index.html' )

def welcome(request):
    return render(request, 'welcome.html')

def register(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('welcome')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Password not match'})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect '
                })
        else:
            login(request, user)
            return redirect('welcome')

def signout(request):
    logout(request)
    return redirect('home')
