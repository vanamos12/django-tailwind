from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _ 

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('libele', 'description', 'prix', 'stock')
    list_filter = ('libele', 'prix')
    fieldsets = (
        (_('Product information'), {'fields': ('libele', 'description', 'prix', 'stock')}),
    )

    search_fields = ('libele', 'prix')
    ordering = ('prix',)

admin.site.register(Product, ProductAdmin)