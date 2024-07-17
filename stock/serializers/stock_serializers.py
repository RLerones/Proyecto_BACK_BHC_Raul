from rest_framework import serializers
from stock.models import Stock

# Serializer para el modelo Stock
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
