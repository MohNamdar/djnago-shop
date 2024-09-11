from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product


@receiver(pre_save, sender=Product)
def calculate_price(sender, instance, **kwargs):
    if not instance.new_price:
        instance.new_price = instance.price - instance.off
    else:
        instance.off = instance.price - instance.new_price
