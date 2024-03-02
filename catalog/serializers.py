from rest_framework import serializers
from .models import Catalog, BinanceData

class BinanceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinanceData
        fields = '__all__'




class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
