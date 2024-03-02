from celery import shared_task
from .models import BinanceData
import requests
from datetime import datetime

@shared_task
def get_binance_data():
    response = requests.get('https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT')
    data = response.json()
    print(data)
    BinanceData.objects.create(
        time=datetime.now(),
        price=data['lastPrice'],
        volume=data['volume'],
        coin='BTCUSDT'
    )




