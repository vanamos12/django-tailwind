from django.db import models
from django.contrib.auth.models import AbstractUser


user_in_migrattion = True
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('clients', 'Client'), 
        ('sellers', 'Seller')
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='clients'
    )
