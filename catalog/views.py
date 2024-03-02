from rest_framework import viewsets
from .models import Catalog
from .serializers import CatalogSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


from django.shortcuts import render
from .models import BinanceData
import json

def bitcoin_chart(request):
    bitcoin_prices = BinanceData.objects.all().order_by('time')
    bitcoin_prices_json = json.dumps([{
        'price': price.price,
        'timestamp': price.time.isoformat()
    } for price in bitcoin_prices])
    return render(request, 'bitcoin.html', {'bitcoin_prices_json': bitcoin_prices_json})
