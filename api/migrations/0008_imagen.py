# Generated by Django 4.2.7 on 2024-04-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_usuarioempresa_ruc"),
    ]

    operations = [
        migrations.CreateModel(
            name="Imagen",
            fields=[
                ("id_imagen", models.AutoField(primary_key=True, serialize=False)),
                ("imagen", models.ImageField(upload_to="imagenes/")),
            ],
        ),
    ]