# Generated by Django 4.2.7 on 2024-11-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0040_alter_centroacopio_id_centro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="centroacopio",
            name="id_centro",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
