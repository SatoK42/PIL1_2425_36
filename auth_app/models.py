from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    photo = models.ImageField(upload_to='photos_de_profil/', blank=True, null=True)

    phone_number = PhoneNumberField(unique=True, region='BJ')
    ROLE_CHOICES = [('conducteur','Conducteur'), ('passager','Passager')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = [] 