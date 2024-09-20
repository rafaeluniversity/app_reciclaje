# Generated by Django 4.2.7 on 2024-09-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0024_solicitudescanceladas"),
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
                    ("CR", "Cancelada Reciclador"),
                    ("CU", "Cancelada Usuario"),
                    ("FC", "Fin Cancelada"),
                    ("F", "Fin"),
                ],
                max_length=2,
            ),
        ),
    ]
