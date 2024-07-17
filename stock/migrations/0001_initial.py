# Generated by Django 5.0.6 on 2024-07-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]
