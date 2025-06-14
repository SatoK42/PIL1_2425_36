from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)

    def __str__(self):
        return f"Profil de {self.user.email}"
