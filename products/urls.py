from django.urls import path
from .views import all_product, product_upload,table_products, delet_product,detaille_product,update_product

# Les path
urlpatterns = [
    path('', all_product, name='allproduct'),
    path('upload/', product_upload, name='upload'),
    path('table/', table_products, name='table' ),
    path('delet/<int:id>/' , delet_product, name='delet_product'),
    path('detaille/<int:id>/' , detaille_product, name='detaille'),
    path('update/<int:id>/', update_product, name='update')
]
