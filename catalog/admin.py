from django.contrib import admin
from .models import Catalog, BinanceData, Coin


# Register your models here.
admin.site.register(Catalog)
admin.site.register(BinanceData)
admin.site.register(Coin)

