from django import forms
from .models import Product

#class ProductForm(forms.ModelForm):
    
#    class Meta:
#        model = Product
#        fields = ['libele', 'description', 'prix', 'image','stock']


class ProductForm(forms.Form):
    libele = forms.CharField(required=True, max_length=100, min_length=2, label='Entrer le Libelé', widget=forms.TextInput(
        attrs={
            'class': 'libele form-control',
            'placeholder': 'Entrer le libelé du produit',
            'id': 'libele',
            'name': 'libele'}))
    description = forms.CharField(required=True, label='Description', max_length=3000, min_length=1, widget=forms.Textarea(
        attrs={
            'class': 'description form-control',
            'placeholder': 'Entrer la description du produit',
            'id': 'description',
            'name': 'description'}))
    prix = forms.DecimalField(required=True, label='Prix', max_digits=10, decimal_places=2 , widget=forms.NumberInput(
        attrs={
            'class': 'prix form-control',
            'placeholder': 'Entrer le prix du produit',
            'id': 'prix',
            'name': 'prix'}))
    image = forms.ImageField(required=True, label='Image', widget=forms.FileInput(
        attrs={
            'class': 'image form-control',
            'id': 'image',
            'name': 'image'})   )
    stock = forms.IntegerField(required=True, label='Stock', widget=forms.NumberInput(
        attrs={
            'class': 'stock form-control',
            'placeholder': 'Entrer le stock du produit',
            'id': 'stock',
            'name': 'stock'}))