from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    is_driver = models.BooleanField(default=False)

    VEHICLE_CHOICES = [
        ('moto', 'Moto'),
        ('voiture', 'Voiture'),
    ]
    vehicle_type = models.CharField(
        max_length=10,
        choices=VEHICLE_CHOICES,
        null=True, blank=True,
        help_text="Type de véhicule si vous êtes conducteur."
    )
    seats = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Nombre de places (important) si vous êtes conducteur."
    )
    brand = models.CharField(max_length=100, null=True, blank=True, help_text="Marque du véhicule (facultatif).")
    model = models.CharField(max_length=100, null=True, blank=True, help_text="Modèle du véhicule (facultatif).")

    departure_time = models.TimeField(null=True, blank=True, help_text="Heure de départ habituelle.")
    departure_lat = models.FloatField(null=True, blank=True)
    departure_lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Profil de {self.user.email}"
