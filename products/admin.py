from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ('libele', 'description', 'prix', 'stock','image')
    list_filter = ('libele', 'prix')

    fieldsets = (
        ('Product information', {
            'fields': ('libele', 'description', 'prix', 'stock','image')
        }),
    )

    search_fields = ('libele', 'prix')
    ordering = ('prix',)


admin.site.register(Product, ProductAdmin)
