from django.contrib.auth.models import AbstractUser
from django.db import models

categories_choices = [
    ("Toys", "toys"),
    ("Fashion", "fashion")]
class User(AbstractUser):
    pass



class Listing(models.Model):
    title = models.TextField(max_length=64, blank=False)
    description = models.TextField(max_length=2000, blank=False)
    image_url = models.TextField(blank=True)
    categories = models.CharField(
        max_length=10,
        choices=categories_choices,
        default="Toys"
    )
    
    
    ...
