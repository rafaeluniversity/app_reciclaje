# Generated by Django 4.2.7 on 2024-08-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0019_solicitudrechazada"),
    ]

    operations = [
        migrations.AddField(
            model_name="solicituddetalle",
            name="ubicacion_reciclador",
            field=models.JSONField(
                blank=True,
                help_text="Ubicación del reciclador como lista [latitud, longitud]",
                null=True,
            ),
        ),
    ]
