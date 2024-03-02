from rest_framework import viewsets
from .models import Catalog, BinanceData
from .serializers import CatalogSerializer, BinanceDataSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class BinanceDataViewSet(viewsets.ModelViewSet):
    queryset = BinanceData.objects.all()
    serializer_class = BinanceDataSerializer



from django.shortcuts import render
from .models import BinanceData
import json

def bitcoin_chart(request):
    bitcoin_prices = BinanceData.objects.all().order_by('time')
    bitcoin_prices_json = json.dumps([{
        'price': str(item.price),
        'timestamp': item.time.isoformat()
    } for item in bitcoin_prices])
    return render(request, 'bitcoin.html', {'bitcoin_prices_json': bitcoin_prices_json})
