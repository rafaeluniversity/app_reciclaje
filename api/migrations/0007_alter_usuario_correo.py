# Generated by Django 4.2.7 on 2024-01-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_usuario_clave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]