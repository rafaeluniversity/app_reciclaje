# Generated by Django 4.2.7 on 2023-12-20 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
