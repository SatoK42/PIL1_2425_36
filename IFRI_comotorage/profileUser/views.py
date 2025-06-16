from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django import forms
@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profileUser/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Ton profil a bien été mis à jour.")
            return redirect('profileUser:profile')
        else:
            messages.error(request, "Merci de corriger les erreurs ci-dessous.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profileUser/profile_edit.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def profile_update_vehicle(request):
    profile = request.user.profile
    # Sous-classe pour n’inclure que les champs véhicule
    class VehicleForm(ProfileUpdateForm):
        class Meta(ProfileUpdateForm.Meta):
            fields = ['is_driver', 'vehicle_type', 'seats', 'brand', 'model']
            widgets = {
                'is_driver': forms.HiddenInput(),
                'vehicle_type': forms.Select(attrs={'class': 'form-select', 'id': 'id_vehicle_type'}),
                'seats': forms.NumberInput(attrs={'class': 'form-input', 'min': 1, 'id': 'id_seats'}),
                'brand': forms.TextInput(attrs={'class': 'form-input', 'id': 'id_brand'}),
                'model': forms.TextInput(attrs={'class': 'form-input', 'id': 'id_model'}),
            }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Forcer la valeur initiale de is_driver à True
            self.fields['is_driver'].initial = True
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=profile)
        # Forcer is_driver=True (l’utilisateur s’est déclaré conducteur)
        profile.is_driver = True
        if form.is_valid():
            form.save()
            # Supprimer le flag pour ne plus afficher le modal
            request.session.pop('require_vehicle_info', None)
            messages.success(request, "Informations véhicule enregistrées.")
            return redirect('acceuil')
        else:
            # Réafficher l’accueil avec modal et erreurs
            ctx = {'require_vehicle_info': True, 'vehicle_form': form}
            # Ajoutez ici d’autres variables de contexte nécessaires pour acceuil
            return render(request, 'auth_app/acceuil.html', ctx)
    return redirect('acceuil')


