# Generated by Django 4.2.7 on 2024-09-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0033_remove_centroacopio_imageurl"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parrafo",
            name="imageURL",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="seccion",
            name="imageURL",
            field=models.URLField(blank=True, null=True),
        ),
    ]