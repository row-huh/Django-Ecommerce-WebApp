from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    class Categories(models.TextChoices):
        TOYS = 'TO', 'Toys'
        HOME = 'HO', 'Home'
    
    title = models.TextField(max_length=64, blank=False, unique=True)
    description = models.TextField(max_length=2000, blank=False)
    imageURL = models.TextField(max_length=64, blank=True)
    

    categories = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.TOYS,
    )
    
    
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    context = models.TextField(max_length=500, blank=True)