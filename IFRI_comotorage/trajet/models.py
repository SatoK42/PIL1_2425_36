from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Trajet(models.Model):
    ROLE_CHOICES = [
        ('conducteur', 'Conducteur'),
        ('passager', 'Passager'),
    ]
    STATUS_CHOICES = [
        ('open', 'Ouvert'),
        ('matched', 'Apparié'),
        ('cancelled', 'Annulé'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='trajets', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    # Trajet quotidien vs ponctuel
    recurring = models.BooleanField(default=False, help_text="True si trajet quotidien")
    date = models.DateField(null=True, blank=True, help_text="Date du trajet pour trajet ponctuel")
    heure = models.TimeField(help_text="Heure de départ")
    # Départ
    lieu_depart = models.CharField(max_length=150)
    latitude_depart = models.FloatField()
    longitude_depart = models.FloatField()
    # Arrivée fixe IFRI UAC (rempli automatiquement)
    lieu_arrivee = models.CharField(max_length=150, editable=False)
    latitude_arrivee = models.FloatField(editable=False)
    longitude_arrivee = models.FloatField(editable=False)
    # Places (pertinent si role=conducteur)
    nb_places = models.PositiveIntegerField(null=True, blank=True)
    commentaire = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.recurring and self.date is None:
            raise ValidationError("La date doit être spécifiée pour un trajet ponctuel.")
        if self.recurring and self.date is not None:
            raise ValidationError("Ne spécifiez pas de date pour un trajet quotidien.")
    
    def save(self, *args, **kwargs):
        # Remplir automatiquement la destination IFRI UAC
        from django.conf import settings
        self.lieu_arrivee = settings.IFRI_UAC_NAME
        self.latitude_arrivee = settings.IFRI_UAC_LATITUDE
        self.longitude_arrivee = settings.IFRI_UAC_LONGITUDE
        # Validation
        self.full_clean(exclude=['lieu_arrivee', 'latitude_arrivee', 'longitude_arrivee'])
        super().save(*args, **kwargs)

    def __str__(self):
        desc = "Quotidien" if self.recurring else f"{self.date}"
        return f"{self.user.username} - {self.role} - Départ {self.heure} ({desc})"

class Match(models.Model):
    offre = models.ForeignKey(Trajet, related_name='matches_offre', on_delete=models.CASCADE)
    demande = models.ForeignKey(Trajet, related_name='matches_demande', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('offre', 'demande')

    def __str__(self):
        return f"Match Offre #{self.offre.id} - Demande #{self.demande.id}"

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"