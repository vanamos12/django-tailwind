from django.shortcuts import render, redirect
from django.forms import forms
from .forms import ProductForm
from .models import Product

# Create your views here.
def all_product(request):
    products = Product.objects.all()
    return render(request, 'products/produits.html', {'products': products})    



def product_upload(request):
    if request.method =='POST':
        form= ProductForm(request.POST, request.FILES)
        if form.is_valid():
        
            form.save()
            return redirect('allproduct')
    else:
        form= ProductForm()
    return render(request, 'products/upload.html', {'form': form})
        
