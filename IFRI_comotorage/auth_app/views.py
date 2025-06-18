from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .form import EmailOrPhoneAuthenticationForm, UserModelForm
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from .models import Users
from django.contrib.auth.decorators import login_required
from profileUser.forms import ProfileUpdateForm
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
        user = form.get_user()
        auth_login(request, user)
        # Gérer le flag modal véhicule
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = None
        if profile and profile.is_driver and (not profile.vehicle_type or not profile.seats):
            request.session['require_vehicle_info'] = True
        else:
            request.session.pop('require_vehicle_info', None)
        return redirect('acceuil')
    return render(request, 'auth_app/login.html', {'form': form})

def acceuil(request):
    ctx = {}
    if request.user.is_authenticated and request.session.get('require_vehicle_info'):
        profile = request.user.profile
        # Sous-classe de ProfileUpdateForm pour ne garder que les champs véhicule
        class VehicleForm(ProfileUpdateForm):
            class Meta(ProfileUpdateForm.Meta):
                fields = ['vehicle_type', 'seats', 'brand', 'model']
        # Instancier avec l’instance profile (normalement vides)
        vehicle_form = VehicleForm(instance=profile)
        ctx['require_vehicle_info'] = True
        ctx['vehicle_form'] = vehicle_form
    # Ajoutez ici vos autres clés de contexte pour l’accueil si besoin
    return render(request, 'auth_app/acceuil.html', ctx)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/auth/login/')

