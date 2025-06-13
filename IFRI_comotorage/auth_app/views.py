from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .form import EmailOrPhoneAuthenticationForm, UserModelForm
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from .models import Users


def register(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserModelForm()
    return render(request, 'auth_app/register.html', {'form': form})

def login_view(request):
    form = EmailOrPhoneAuthenticationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_login(request, form.get_user())
        return redirect('acceuil')
    return render(request, 'auth_app/login.html', {'form': form})

def profile(request):
    return render(request, 'auth_app/profile.html')

def acceuil(request):
    return render(request, 'auth_app/acceuil.html')

def edit(request):
    return render(request, 'auth_app/edit.html')

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/auth/login1/')
