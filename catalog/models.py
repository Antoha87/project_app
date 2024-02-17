from django.db import models


class Catalog(models.Model):
    name = models.CharField('Catalog', max_length=100)
