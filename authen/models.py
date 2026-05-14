from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    choix=(
        ('client','Client'),
        ('vendeur','Vendeur')
    )
    role= models.CharField(max_length=20, choices=choix, default='client')
    phone = models.CharField(max_length=20, default='')


class PhoneOTP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='phone_otps')
    code_hash = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    verified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at
