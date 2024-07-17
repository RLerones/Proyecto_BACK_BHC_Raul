from rest_framework import viewsets
from stock.models import Stock
from stock.serializers.stock_serializers import StockSerializer
from stock.filters_sets.stock_filters import StockFilter
from django_filters.rest_framework import DjangoFilterBackend

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StockFilter


