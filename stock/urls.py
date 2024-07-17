from django.urls import path
from stock.views.stock_views import StockViewSet

# Rutas para el modelo Stock
urlpatterns = [
    path('stock', StockViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('stock/<str:pk>', StockViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

