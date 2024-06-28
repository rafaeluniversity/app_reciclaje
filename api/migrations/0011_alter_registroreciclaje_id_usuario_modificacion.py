# Generated by Django 4.2.7 on 2024-05-02 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_tipomaterial_registroreciclaje"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registroreciclaje",
            name="id_usuario_modificacion",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usuario_modificacion",
                to="api.usuario",
            ),
        ),
    ]
