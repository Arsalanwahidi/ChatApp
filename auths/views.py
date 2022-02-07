from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .form import UserInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.backends import ModelBackend, BaseBackend, RemoteUserBackend, AllowAllUsersRemoteUserBackend


# Create your views here.

@login_required(login_url='accounts/login/')
def index(request):
    
    user = User()
    username = user.get_username()
    return render(request, 'auth/base.html', {'username': username, 'cleanUsername': 'clean_username'})

def Sign_up(request):

    signUpForm = UserCreationForm(request.POST)
    if request.POST:
        if signUpForm.is_valid:
            signUpForm.save()
            return redirect('index')
    else:
        signUpForm = UserCreationForm(request.POST)
    return render(request, 'registration/signup.html', {'signUpForm': signUpForm})




