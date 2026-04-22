from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator

# Create your models here.
class Product(models.Model):
    libele = models.CharField(max_length=100, validators=[MinLengthValidator(2, message='le nombre de caractere doit etre superieur a deux')], null=False, blank=False)
    description = models.CharField(max_length=100, validators=[MinLengthValidator(2, message='le nombre de caractere doit etre superieur a deux')], null=False, blank=False)
    profil  = models.ImageField(upload_to='image/profils/', null= True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])])