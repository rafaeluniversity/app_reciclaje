# Generated by Django 4.2.7 on 2024-04-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_usuarioempresa_redes"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuariopersona",
            name="cedula",
            field=models.CharField(default=0, max_length=13, unique=True),
            preserve_default=False,
        ),
    ]
