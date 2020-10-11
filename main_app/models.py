from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    avatar = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username

# Create your models here.
