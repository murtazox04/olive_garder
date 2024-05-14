import json
from django.dispatch import receiver
from django.forms import model_to_dict
from django.db.models.signals import post_save, pre_delete

from config.producer import producer
from apps.cart.models import Cart, CartItem


def send_to_producer(topic, instance):
    data = model_to_dict(instance)
    json_data = json.dumps(data)
    producer.produce(topic, json_data)


@receiver(post_save, sender=Cart)
def cart_saved(sender, instance, created, **kwargs):
    if created:
        send_to_producer("cart_created", instance)
    else:
        send_to_producer("cart_updated", instance)


@receiver(pre_delete, sender=Cart)
def cart_deleted(sender, instance, **kwargs):
    send_to_producer("cart_deleted", instance)


@receiver(post_save, sender=CartItem)
def cart_item_saved(sender, instance, created, **kwargs):
    if created:
        send_to_producer("cart_item_created", instance)
    else:
        send_to_producer("cart_item_updated", instance)


@receiver(pre_delete, sender=CartItem)
def cart_item_deleted(sender, instance, **kwargs):
    send_to_producer("cart_item_deleted", instance)
