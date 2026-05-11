from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from products.models import Product

User = get_user_model()

@receiver(post_migrate)
def create_roles_and_permissions(sender, **kwargs):
    pass