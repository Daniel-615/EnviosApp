# Generated by Django 5.1.1 on 2024-10-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envios_app', '0002_asignacionvehiculotransportista_activo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='asignado',
            field=models.BooleanField(default=False),
        ),
    ]
