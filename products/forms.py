from django import forms
from .models import Product

# class ProductForm(forms.ModelForm):
    
#     class Meta:
#         model = Product
#         fields = ['libele', 'description', 'prix', 'image','stock']

from django import forms

# class ProductForm(forms.Form):

#     libele = forms.CharField(
#         required=True,
#         label='Entrer le libellé',
#         max_length=50,
#         min_length=4,
#         widget=forms.TextInput(attrs={
#             'class': 'libele'
#         })
#     )

#     description = forms.CharField(
#         required=True,
#         label='Entrer la description',
#         max_length=200,
#         widget=forms.Textarea(attrs={
#             'class': 'description'
#         })
#     )

#     prix = forms.DecimalField(
#         required=True,
#         label='Entrer le prix',
#         max_digits=10,
#         decimal_places=2,
#         widget=forms.NumberInput(attrs={
#             'class': 'prix'
#         })
#     )

#     image = forms.ImageField(
#         required=True,
#         label='Image du produit',
#         widget=forms.FileInput(attrs={
#             'class': 'image'
#         })
#     )

#     stock = forms.IntegerField(
#         required=True,
#         label='Quantité en stock',
#         widget=forms.NumberInput(attrs={
#             'class': 'stock'
#         })
#     )

# 
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['libele', 'description', 'prix', 'image', 'stock']

        widgets = {
            'libele': forms.TextInput(attrs={'class': 'libele'}),
            'description': forms.Textarea(attrs={'class': 'description'}),
            'prix': forms.NumberInput(attrs={'class': 'prix'}),
            'image': forms.FileInput(attrs={'class': 'image'}),
            'stock': forms.NumberInput(attrs={'class': 'stock'}),
        }