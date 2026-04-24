from django.urls import path
from .views import all_product, product_upload, product_update, product_delete, product_detail

# Les path
urlpatterns = [
    path('', all_product, name='allproduct'),
    path('upload/', product_upload, name='upload'),
    path('update/<int:id>/', product_update, name='product_update'),
    path('delete/<int:id>/', product_delete, name='product_delete'),    
    path('detail/<int:id>/', product_detail, name='product_detail'),
]