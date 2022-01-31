from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .form import UserInfoForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required
def index(request):
    
    return render(request, 'auth/index.html', {})

def Sign_up(request):

    signUpForm = UserCreationForm(request.POST)
    if request.POST:
        if signUpForm.is_valid:
            signUpForm.save()
            return redirect('index')
    else:
        signUpForm = UserCreationForm(request.POST)
    return render(request, 'registration/signup.html', {'signUpForm': signUpForm})




