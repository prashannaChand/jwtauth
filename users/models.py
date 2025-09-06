from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username =None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []    
    
    def __str__(self):
        return self.email