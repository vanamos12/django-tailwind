from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['libele', 'description', 'prix', 'image','stock']
