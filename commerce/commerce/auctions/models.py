from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.TextField(max_length=64, blank=False)
    description = models.TextField(max_length=2000, blank=False)
    imageURL = models.TextField(max_length=64, blank=True)
    categories = models.TextChoices("toys", "fashion")
    # bid
    
