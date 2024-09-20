# Generated by Django 4.2.7 on 2024-09-18 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0028_alter_calificacion_id_usuario_calificado_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solicitudescanceladas",
            name="id_usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usuario_cancela",
                to="api.usuario",
            ),
        ),
    ]
