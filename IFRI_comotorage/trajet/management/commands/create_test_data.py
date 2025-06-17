from django.core.management.base import BaseCommand
from auth_app.models import Users
from trajet.models import Trajet

class Command(BaseCommand):
    help = 'Crée des données de test pour les utilisateurs et les trajets.'

    def handle(self, *args, **kwargs):
        # Créer des utilisateurs de test
        conducteur1, created = Users.objects.get_or_create(
            username='conducteur1',
            defaults={
                'password': 'password123',
                'email': 'conducteur1@example.com',
                'first_name': 'Jean',
                'last_name': 'Dupont'
            }
        )
        if created:
            conducteur1.set_password('password123')
            conducteur1.save()

        passager1, created = Users.objects.get_or_create(
            username='passager1',
            defaults={
                'password': 'password123',
                'email': 'passager1@example.com',
                'first_name': 'Marie',
                'last_name': 'Martin'
            }
        )
        if created:
            passager1.set_password('password123')
            passager1.save()

        # Créer des trajets de test
        Trajet.objects.get_or_create(
            user=conducteur1,
            depart='Paris',
            arrivee='Lyon',
            date_depart='2023-10-01',
            heure_depart='08:00',
            role='conducteur'
        )

        Trajet.objects.get_or_create(
            user=passager1,
            depart='Paris',
            arrivee='Lyon',
            date_depart='2023-10-01',
            heure_depart='08:00',
            role='passager'
        )

        self.stdout.write(self.style.SUCCESS('Données de test créées avec succès.')) 