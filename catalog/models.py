from django.db import models


class Catalog(models.Model):
    name = models.CharField('Catalog', max_length=100)
    active = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name

