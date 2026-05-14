from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import forms
from .forms import ProductForm
from .models import Product
from django.core.paginator import Paginator
from django.contrib import auth

# Create your views here.
@login_required(login_url='/', redirect_field_name='login')
@permission_required(perm='can_view_all_products')
def all_product(request):
    if request.user.has_perm('product.can_view_all_product'):
        products= Product.objects.all()
    
    return render(request, 'products/produits.html', {"products": products})

@login_required(login_url='/', redirect_field_name='login')
@permission_required(perm='products.add_product')
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
    liste= Product.objects.all().order_by('-id')
    pagination= Paginator(liste, 6)
    number_page= request.GET.get('page')
    products=pagination.get_page(number_page)
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
    
