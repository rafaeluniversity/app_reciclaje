# Generated by Django 4.2.7 on 2024-01-02 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_reciclador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id_archivo', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudRecoleccion',
            fields=[
                ('id_solicitud', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=1000)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aceptada'), ('C', 'Cancelada'), ('F', 'Fallida'), ('E', 'Entregada')], max_length=1)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_asig', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('id_reciclador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reciclador')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ReporteDenuncias',
            fields=[
                ('id_reporte', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=1000)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], max_length=1)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('resolucion', models.CharField(blank=True, max_length=1000, null=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denuncias_realizadas', to='api.usuario')),
                ('id_usuario_rep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denuncias_recibidas', to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField()),
                ('observacion', models.CharField(max_length=1000)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_reciclador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones_reciclador', to='api.reciclador')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ArchivosSolicitudes',
            fields=[
                ('id_archivo_solicitud', models.BigAutoField(primary_key=True, serialize=False)),
                ('archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.archivo')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.solicitudrecoleccion')),
            ],
        ),
        migrations.CreateModel(
            name='ArchivosReportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.archivo')),
                ('id_reporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reportedenuncias')),
            ],
        ),
        migrations.CreateModel(
            name='CarnetRecolectores',
            fields=[
                ('id_archivo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.archivo')),
                ('id_recolector', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.reciclador')),
            ],
        ),
    ]