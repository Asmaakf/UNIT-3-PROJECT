from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=50)
    university = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username





               
