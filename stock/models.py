from django.db import models

# Modelo Stock
class Stock(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    quantity = models.IntegerField(verbose_name="Cantidad")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    class Meta:
        db_table = 'stock'  # Nombre de la tabla en la base de datos

