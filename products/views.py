from django.shortcuts import render
from .models import Product

# Create your views here.

def allproducts(request):

    # form = ContactForm(request.POST, request.FILES)
    products = Product.objects.all()
    
    return render(request=request, template_name='products.html', context={'products': products })