from django_filters import rest_framework as filters
from stock.models import Stock

class StockFilter(filters.FilterSet):
    class Meta:
        model = Stock
        fields = {
            'name': ['icontains'],
            'quantity': ['gte', 'lte'],
            'price': ['gte', 'lte'],
        }
