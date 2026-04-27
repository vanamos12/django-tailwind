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
        
            #form.save()
            Product.objects.create(
                libele=form.cleaned_data.get('libele'),
                description=form.cleaned_data.get('description'),
                prix=form.cleaned_data.get('prix'),
                image=form.cleaned_data.get('image'),
                stock=form.cleaned_data.get('stock')
            )
            return redirect('allproduct')
    else:
        form= ProductForm()
    return render(request, 'products/upload.html', {'form': form})
        
def product_update(request, id):
    product = Product.objects.get(id=id)
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.libele = form.cleaned_data.get('libele')
            product.description = form.cleaned_data.get('description')  
            product.prix = form.cleaned_data.get('prix')
            product.image = form.cleaned_data.get('image')  
            product.stock = form.cleaned_data.get('stock')
            product.save()
            return redirect('allproduct')
        else:
            return 
        
    else:
        #form = ProductForm(instance=product)
        pass
    return render(request, 'products/upload.html', {'product': product})

def product_delete(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
    
    return redirect('allproduct')

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/detail.html', {'product': product})