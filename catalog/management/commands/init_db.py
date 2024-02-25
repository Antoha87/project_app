import requests
from django.core.management.base import BaseCommand
from catalog.models import Catalog

class Command(BaseCommand):

    def handle(self):
        url = 'https://dummyjson.com/products'
        resp = requests(url)
        for item in resp.json():
            Catalog.objects.create(name=item['name'], description=item['description'])
