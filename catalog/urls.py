from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatalogViewSet, bitcoin_chart, BinanceDataViewSet

router = DefaultRouter()
router.register(r'catalog', CatalogViewSet)
router.register(r'bitcoin', BinanceDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bitcoin-chart/', bitcoin_chart, name='bitcoin_chart'),
]
