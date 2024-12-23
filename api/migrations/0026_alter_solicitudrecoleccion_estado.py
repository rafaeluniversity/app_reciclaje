# Generated by Django 4.2.7 on 2024-09-15 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0025_alter_solicitudrecoleccion_estado"),
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
                    ("R", "Recolectada"),
                    ("CR", "Cancelada Reciclador"),
                    ("CU", "Cancelada Usuario"),
                    ("FC", "Fin Cancelada"),
                    ("F", "Fin"),
                ],
                max_length=2,
            ),
        ),
    ]
