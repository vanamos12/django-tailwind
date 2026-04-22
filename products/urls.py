from django.urls import path
from .views import allproducts

urlpatterns = [
    path('', allproducts, name='products')
]
