from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class Users(AbstractUser):
    username = None
    email = models.EmailField('email address', max_length=191, unique=True)

    phone_number = PhoneNumberField(unique=True, region='BJ')
    ROLE_CHOICES = [('conducteur','Conducteur'), ('passager','Passager')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 


    