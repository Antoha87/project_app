from django.db import models


class Catalog(models.Model):
    name = models.CharField('Catalog', max_length=100)
    active = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Catalogs'
        ordering = ['name']
        verbose_name = 'Catalog'


class BinanceData(models.Model):
    time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    coin = models.CharField(max_length=100)

    def __str__(self):
        return self.coin

    class Meta:
        verbose_name_plural = 'Binance Data'
        ordering = ['time']
        verbose_name = 'Binance Data'
