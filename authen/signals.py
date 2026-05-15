from django.db.models.signals import post_migrate, post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from products.models import Product

User = get_user_model()

@receiver(post_migrate)
def create_roles_and_permissions(sender, **kwargs):
    clients_group, create = Group.objects.get_or_create(name='clients')

    if create:
        print('role creer')
    else:
        print('le role existe deja')

    sellers_group, _ = Group.objects.get_or_create(name='sellers')

    contentType = ContentType.objects.get_for_model(Product)

    can_view_all_product, _ = Permission.objects.get_or_create(codename='can_view_all_products', name='Can view all product', content_type=contentType)


    clients_group.permissions.add(can_view_all_product)
    # admin_group.permissions.set([can_view_all_product, creat_product,])


@receiver(post_save, sender=User)
def assign_user_to_groupe(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'sellers':
            seller_group, _ = Group.objects.get_or_create(name='sellers')
            instance.groups.add(seller_group)
            instance.save()
        elif instance.role == "clients":
            clients_group, _ = Group.objects.get_or_create(name='clients')
            instance.groups.add(clients_group)
            instance.save()