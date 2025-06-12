from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .form import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil après connexion
        else:
            return render(request, 'login.html', {'error': 'Email ou mot de passe incorrect'})
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def acceuil(request):
    return render(request, 'acceuil.html')

def edit(request):
    return render(request, 'edit.html')