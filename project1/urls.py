
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [ path('api/token/', include("users.token_urls")),
    path('api/', include("users.urls"))]

urlpatterns += [
    path('api/', include('stock.urls')), #incluir las rutas de la app stock

    # Endpoint para el esquema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Documentación interactiva con Swagger
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Documentación interactiva con Redoc
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

