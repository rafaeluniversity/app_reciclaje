# Generated by Django 4.2.7 on 2024-07-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_remove_centroacopio_lat_remove_centroacopio_lon_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="centroacopio",
            name="ubicacion",
            field=models.JSONField(
                help_text="Ubicación como lista [latitud, longitud]"
            ),
        ),
    ]
