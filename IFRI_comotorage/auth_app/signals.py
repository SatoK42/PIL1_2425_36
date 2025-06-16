from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse

@receiver(user_logged_in)
def check_driver_info(sender, user, request, **kwargs):
    """
    Après login, si l'utilisateur est conducteur et que les champs véhicule
    ne sont pas renseignés (vehicle_type ou seats manquants),
    on place un flag en session pour afficher le modal.
    """
    profile = getattr(user, 'profile', None)
    if profile:
        # Condition pour forcer la saisie : is_driver True mais infos manquantes
        if profile.is_driver and (not profile.vehicle_type or not profile.seats):
            # Mettre un flag en session
            request.session['require_vehicle_info'] = True
        else:
            # Nettoyer le flag s'il existait
            request.session.pop('require_vehicle_info', None)
