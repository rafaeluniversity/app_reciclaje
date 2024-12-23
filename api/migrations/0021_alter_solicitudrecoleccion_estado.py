# Generated by Django 4.2.7 on 2024-09-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_solicituddetalle_ubicacion_reciclador"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solicitudrecoleccion",
            name="estado",
            field=models.CharField(
                choices=[
                    ("P", "Pendiente"),
                    ("A", "Aceptada"),
                    ("L", "Cerca"),
                    ("C", "Cancelada"),
                    ("F", "Fallida"),
                    ("E", "Entregada"),
                ],
                max_length=1,
            ),
        ),
    ]
