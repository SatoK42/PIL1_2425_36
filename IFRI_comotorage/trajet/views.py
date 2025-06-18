from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import JsonResponse
from .forms import TrajetForm
from .models import Trajet, Match, Notification
from .algo.matching import gale_shapley
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.conf import settings
import logging
logger = logging.getLogger(__name__)


@login_required
def dashboard(request):
    user = request.user
    cache_key = f"matches_{user.id}"
    logger.info("Dashboard accès méthode %s par user %s", request.method, user.id)

    if request.method == 'POST':
        form = TrajetForm(request.POST, user=user)
        logger.info("POST reçu, form.is_valid()=%s", form.is_valid())
        logger.info("Valeur mode reçue en POST: %s", request.POST.get('mode'))
        if form.is_valid():
            try:
                trajet = form.save(user=user)
                logger.info("Trajet créé id=%s recurring=%s lat=%s lng=%s heure=%s",
                            trajet.id, trajet.recurring,
                            trajet.latitude_depart, trajet.longitude_depart,
                            trajet.heure)
            except Exception as e:
                logger.error("Erreur save Trajet: %s", e)
                form.add_error(None, str(e))
            else:
                # matching
                cache.delete(cache_key)
                trajets_all = Trajet.objects.filter(status='open')
                drivers = [t for t in trajets_all if t.role == 'conducteur']
                passengers = [t for t in trajets_all if t.role == 'passager']
                drivers_dict = [
                    {'id': t.id,
                     'latitude': t.latitude_depart,
                     'longitude': t.longitude_depart,
                     'heure_depart': t.heure.hour*60 + t.heure.minute}
                    for t in drivers
                ]
                passengers_dict = [
                    {'id': t.id,
                     'latitude': t.latitude_depart,
                     'longitude': t.longitude_depart,
                     'heure_depart': t.heure.hour*60 + t.heure.minute}
                    for t in passengers
                ]
                logger.info("Drivers pour matching: %s", drivers_dict)
                logger.info("Passengers pour matching: %s", passengers_dict)
                matches_map = gale_shapley(drivers_dict, passengers_dict)
                logger.info("Résultat gale_shapley: %s", matches_map)
                if trajet.role == 'conducteur':
                    partenaire_id = matches_map.get(trajet.id)
                else:
                    inv = {v: k for k, v in matches_map.items()}
                    partenaire_id = inv.get(trajet.id)
                logger.info("Partenaire trouvé id: %s", partenaire_id)
                if partenaire_id:
                    partenaire_trajet = Trajet.objects.filter(id=partenaire_id, status='open').first()
                    if partenaire_trajet:
                        Notification.objects.create(
                            user=partenaire_trajet.user,
                            message=f"Nouvelle correspondance avec {user.first_name} {user.last_name} pour le trajet #{trajet.id}."
                        )
                        logger.info("Notification créée pour user %s", partenaire_trajet.user.id)
                return redirect('trajet:dashboard')
        if not form.is_valid():
            logger.info("Form invalid, errors: %s", form.errors)
    else:
        form = TrajetForm(user=user)

    trajets = Trajet.objects.filter(user=user).order_by('-created_at')
    notifications = user.notifications.order_by('-created_at')[:10]

    user_matches = cache.get(cache_key)
    if user_matches is None:
        trajets_all = Trajet.objects.filter(status='open')
        drivers = [t for t in trajets_all if t.role == 'conducteur']
        passengers = [t for t in trajets_all if t.role == 'passager']
        drivers_dict = [
            {'id': t.id,
             'latitude': t.latitude_depart,
             'longitude': t.longitude_depart,
             'heure_depart': t.heure.hour*60 + t.heure.minute}
            for t in drivers
        ]
        passengers_dict = [
            {'id': t.id,
             'latitude': t.latitude_depart,
             'longitude': t.longitude_depart,
             'heure_depart': t.heure.hour*60 + t.heure.minute}
            for t in passengers
        ]
        matches_map = gale_shapley(drivers_dict, passengers_dict)
        user_matches = []
        for t in trajets:
            if t.role == 'conducteur':
                partner_id = matches_map.get(t.id)
                if partner_id:
                    partner = next((p for p in passengers if p.id == partner_id), None)
                    if partner:
                        user_matches.append(partner)
            else:
                inv = {v: k for k, v in matches_map.items()}
                partner_id = inv.get(t.id)
                if partner_id:
                    partner = next((d for d in drivers if d.id == partner_id), None)
                    if partner:
                        user_matches.append(partner)
        cache.set(cache_key, user_matches, 300)

    return render(request, 'trajet/dashboard.html', {
        'form': form,
        'trajets': trajets,
        'matches': user_matches,
        'notifications': notifications,
        'IFRI_LAT': settings.IFRI_UAC_LATITUDE,
        'IFRI_LNG': settings.IFRI_UAC_LONGITUDE,
    })



@require_POST
@login_required
def accepter_match(request, trajet_id):
    # trajet_id est l'ID du trajet partenaire
    partenaire_trajet = get_object_or_404(Trajet, id=trajet_id, status='open')
    user = request.user

    # On doit identifier quel trajet est offre / demande.
    # Supposons que l'utilisateur a un trajet ouvert correspondant ; 
    # si l'utilisateur est conducteur, son trajet est offre, sinon demande.
    # Ici, il faut définir précisément : 
    # si un seul trajet actif par user, on peut faire :
    mon_trajet = Trajet.objects.filter(user=user, status='open').first()
    if not mon_trajet:
        return JsonResponse({"error": "Vous n'avez pas de trajet ouvert."}, status=400)

    # Vérifier qu'ils ont des rôles complémentaires
    if mon_trajet.role == partenaire_trajet.role:
        return JsonResponse({"error": "Rôle incompatible pour matching."}, status=400)

    # Déterminer offre et demande
    if mon_trajet.role == 'conducteur':
        offre_obj = mon_trajet
        demande_obj = partenaire_trajet
    else:
        offre_obj = partenaire_trajet
        demande_obj = mon_trajet

    # Créer le Match si pas déjà existant
    match, created = Match.objects.get_or_create(offre=offre_obj, demande=demande_obj)
    if not created:
        return JsonResponse({"error": "Match déjà existant."}, status=400)

    # Mettre à jour le statut si besoin
    offre_obj.status = 'matched'
    demande_obj.status = 'matched'
    offre_obj.save(update_fields=['status'])
    demande_obj.save(update_fields=['status'])

    # Notification à l’autre utilisateur
    autre_user = demande_obj.user if user == offre_obj.user else offre_obj.user
    Notification.objects.create(
        user=autre_user,
        message=f"{user.username} a accepté le trajet (Match #{match.id})."
    )
    return JsonResponse({"success": True})


@require_POST
@login_required
def decliner_match(request, trajet_id):
    partenaire_trajet = get_object_or_404(Trajet, id=trajet_id, status='open')
    user = request.user
    mon_trajet = Trajet.objects.filter(user=user, status='open').first()
    if not mon_trajet or mon_trajet.role == partenaire_trajet.role:
        return JsonResponse({"error": "Impossible de décliner."}, status=400)

    # On peut enregistrer un “refus” en créant un Match avec is_accepted=False, ou simplement ignorer
    if mon_trajet.role == 'conducteur':
        offre_obj = mon_trajet
        demande_obj = partenaire_trajet
    else:
        offre_obj = partenaire_trajet
        demande_obj = mon_trajet

    match, created = Match.objects.get_or_create(offre=offre_obj, demande=demande_obj)
    match.is_accepted = False
    match.save(update_fields=['is_accepted'])
    # Optionnel : notification
    Notification.objects.create(
        user=partenaire_trajet.user,
        message=f"{user.username} a refusé le trajet."
    )
    return JsonResponse({"success": True})

@login_required
def notifications_page(request):
    # Récupérer toutes les notifications non lues et/ou l’historique
    notifications = request.user.notifications.order_by('-created_at')
    return render(request, 'trajet/notifications.html', {
        'notifications': notifications,
    })

@require_POST
@login_required
def marquer_lu(request, notification_id):
    notif = get_object_or_404(Notification, id=notification_id, user=request.user)
    notif.is_read = True
    notif.save(update_fields=['is_read'])
    return redirect('trajet:notifications_page')
