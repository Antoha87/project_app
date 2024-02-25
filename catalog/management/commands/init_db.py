import requests
from django.core.management.base import BaseCommand
from catalog.models import Catalog

class Command(BaseCommand):

    def handle(self, *args, **options):
        url = 'https://dummyjson.com/products'
        resp = requests.get(url)
        for item in resp.json():
            print(item['name'])
            Catalog.objects.create(name=item['name'], description=item['description'])

