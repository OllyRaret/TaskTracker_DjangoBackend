from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.username