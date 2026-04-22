from django.urls import path
from .views import all_product, product_upload

# Les path
urlpatterns = [
    path('', all_product, name='allproduct'),
    path('upload/', product_upload, name='upload')
]
