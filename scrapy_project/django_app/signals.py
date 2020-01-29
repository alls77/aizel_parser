from django.dispatch import receiver, Signal
from django.db.models.signals import post_delete
from channels.layers import get_channel_layer

from django_app.models import Product
from django_app.utils import create_or_use_loop


data_saved = Signal(providing_args=["status"])


@receiver(post_delete, sender=Product)
def delete_price_with_product(sender, instance, **kwargs):
    instance.price.delete()


@receiver(data_saved, sender="parser")
def status_update(sender, **kwargs):
    channel_layer = get_channel_layer()
    group_name = 'products'

    create_or_use_loop(channel_layer.group_send(
        group_name, {
            'type': 'update',
            'update': kwargs["status"],
        })
    )
