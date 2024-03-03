from django.db.models.signals import pre_save
from django.dispatch import receiver
from .tasks import get_current_price
from .models import Coin


@receiver(signal=pre_save, sender=Coin)
def pre_save_coin(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        price = get_current_price(name).delay()
        instance.price = price
        instance.save()
