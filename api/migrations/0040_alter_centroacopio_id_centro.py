# Generated by Django 4.2.7 on 2024-11-09 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0039_centroacopio_organizacion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="centroacopio",
            name="id_centro",
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
