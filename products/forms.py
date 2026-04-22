from django import forms
from .models import Product

# class ProductForm(forms.ModelForm):
    
#     class Meta:
#         model = Product
#         fields = ['libele', 'description', 'prix', 'image','stock']
class ProductForm(forms.Form):
    libele = forms.CharField(required=True, label="Entrer le libele", max_length=30, min_length=1, widget=forms.TextInput(attrs={
        'class':"libele",
        'id':'libele',
        'name':'libele',
    }))
    description = forms.CharField(required=True, label="Entrer la description", max_length=30, min_length=1, widget=forms.TextInput(attrs={
        'class':"description",
        'id':'description',
        'name':'description',
    }))
    prix = forms.DecimalField(required=True, label="Entrer la description", widget=forms.NumberInput(attrs={
        'class':"prix",
        'id':'prix',
        'name':'prix',
    }))