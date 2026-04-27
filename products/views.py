from django.shortcuts import render, redirect, get_object_or_404
from django.forms import forms
from .forms import ProductForm
from .models import Product

# Create your views here.
def all_product(request):
    products= Product.objects.all()
    return render(request, 'products/produits.html', {"products": products})


def product_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('allproduct')  

    else:
        form = ProductForm()

    return render(request, 'products/upload.html', {
        'form': form
    })


def table_products(request):
    products= Product.objects.all()
    return render(request, 'products/table.html', {'produits': products})

def delet_product(request, id):
    product= get_object_or_404(Product, id=id)
    product.delete()
    return redirect('table')

def detaille_product(request, id):
    products= get_object_or_404(Product, id=id)
    return render(request, 'products/detaille.html', {'product': products})

def update_product(request, id):
    product= get_object_or_404(Product, id=id)
    if request.method=='POST':
        form= ProductForm(request.POST, request.FILES ,instance=product )
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
        form= ProductForm(instance=product)
    return render(request,'products/update.html',{'form':form})
    
