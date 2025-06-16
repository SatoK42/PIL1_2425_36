from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

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
