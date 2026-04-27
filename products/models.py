from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator

# Create your models here.
class Product(models.Model):
    libele = models.CharField(max_length=100, validators=[MinLengthValidator(2, message="Le minimun de caractere c'est 2")], null=False, blank=False)
    prix= models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(validators=[MinLengthValidator(10, message="Le nombre de caractere doit suprerieur a 10")])
    stock= models.IntegerField(default=0)
    image= models.ImageField(default=True , upload_to='media')
    created_at=models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libele


    