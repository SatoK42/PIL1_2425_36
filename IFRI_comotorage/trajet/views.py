from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .models import Trajet, Matching, Notification
from .algo.matching import gale_shapley
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

@login_required
def notifications(request):
    user = request.user
    cache_key = f"matches_{user.id}"

    # Vérifier le cache
    user_matches = cache.get(cache_key)
    if not user_matches:
        trajets = Trajet.objects.all()
        drivers = [t for t in trajets if t.role == 'conducteur']
        passengers = [t for t in trajets if t.role == 'passager']

        def trajet_to_dict(t):
            return {
                "id": t.id,
                "nom": t.user.last_name,
                "prenom": t.user.first_name,
                "photo_profile": t.user.profile.photo.url if hasattr(t.user, 'profile') else None,
                "latitude": t.latitude_depart,
                "longitude": t.longitude_depart,
                "heure_depart": t.heure.hour * 60 + t.heure.minute
            }
        drivers_dict = [trajet_to_dict(t) for t in drivers]
        passengers_dict = [trajet_to_dict(t) for t in passengers]

        matches = gale_shapley(drivers_dict, passengers_dict)

        user_matches = []
        # Vérifier si l'utilisateur a des trajets
        user_trajet = user.trajets.first()
        if user_trajet:
            if user_trajet.role == 'conducteur':
                match = matches.get(user.username)
                if match:
                    user_matches = [match]
            else:
                inv_matches = {v: k for k, v in matches.items()}
                match = inv_matches.get(user.username)
                if match:
                    user_matches = [match]

        # Mettre en cache pour 5 minutes
        cache.set(cache_key, user_matches, 300)

    return render(request, "notifications.html", {"matches": user_matches})

@require_POST
@login_required
def accepter_match(request, match_id):
    # Récupérer le trajet correspondant au match_id
    trajet = Trajet.objects.get(id=match_id)
    # Enregistrer le matching
    Matching.objects.create(
        driver=request.user,
        passenger=trajet.user,
        is_accepted=True
    )
    # Envoyer une notification
    Notification.objects.create(
        user=trajet.user,
        message=f"{request.user.username} a accepté le matching !"
    )
    return JsonResponse({"success": True})

@require_POST
@login_required
def decliner_match(request, match_id):
    # Récupérer le trajet correspondant au match_id
    trajet = Trajet.objects.get(id=match_id)
    # Enregistrer le matching
    Matching.objects.create(
        driver=request.user,
        passenger=trajet.user,
        is_accepted=False
    )
    return JsonResponse({"success": True})
