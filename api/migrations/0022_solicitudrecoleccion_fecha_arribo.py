# Generated by Django 4.2.7 on 2024-09-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0021_alter_solicitudrecoleccion_estado"),
    ]

    operations = [
        migrations.AddField(
            model_name="solicitudrecoleccion",
            name="fecha_arribo",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
