from django.contrib import admin
from django.utils.translation import gettext_lazy as _ 

# Register your models here.

from .models import User

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username', 'role', 'email',)
    list_filter = ('is_active',)
    fieldsets = (
        (_('User information'), {'fields': ('username', 'role', 'email', 'password')}),
    )

    search_fields = ('email', 'username')
    ordering = ('username',)

admin.site.register(User, UserAdmin)