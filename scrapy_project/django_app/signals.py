from django.db.models.signals import post_delete
from django.dispatch import receiver

from django_app.models import Product


@receiver(post_delete, sender=Product)
def delete_price_with_product(sender, instance, **kwargs):
    instance.price.delete()
