# Generated by Django 5.1.1 on 2024-10-20 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envios_app', '0002_rename_rastreos_rastreo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignacionvehiculotransportista',
            old_name='transportista',
            new_name='id_transportista',
        ),
        migrations.RenameField(
            model_name='asignacionvehiculotransportista',
            old_name='vehiculo',
            new_name='id_vehiculo',
        ),
    ]
