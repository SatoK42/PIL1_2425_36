from django.db import models
from django.conf import settings

class Trajet(models.Model):
    ROLE_CHOICES = [('conducteur', 'Conducteur'), ('passager', 'Passager')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='trajets', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    lieu_depart = models.CharField(max_length=150)
    lieu_arrivee = models.CharField(max_length=150)
    latitude_depart = models.FloatField()
    longitude_depart = models.FloatField()
    heure = models.TimeField()
    nb_places = models.PositiveIntegerField(null=True, blank=True)
    commentaire = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.lieu_depart} → {self.lieu_arrivee}"