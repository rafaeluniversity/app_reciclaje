# Generated by Django 4.2.7 on 2024-09-20 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0031_usuariotemporal_datos_adicionales"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuariotemporal",
            name="datos_adicionales",
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]