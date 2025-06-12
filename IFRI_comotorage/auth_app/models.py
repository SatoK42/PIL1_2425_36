from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=50),
    last_name = models.CharField(max_length=50),
    password = models.CharField(max_length=20),
    email = models.EmailField(max_length=100, unique=True),
    phone_number = models.CharField(max_length=15, unique=True),
