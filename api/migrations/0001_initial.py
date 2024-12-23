# Generated by Django 4.2.7 on 2024-04-05 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Archivo",
            fields=[
                ("id_archivo", models.BigAutoField(primary_key=True, serialize=False)),
                ("descripcion", models.CharField(max_length=250)),
                ("fecha_subida", models.DateTimeField(auto_now_add=True)),
                ("url", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Roles",
            fields=[
                (
                    "id_rol",
                    models.CharField(
                        max_length=13, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("descripcion", models.CharField(max_length=1000)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id_usuario",
                    models.CharField(max_length=13, primary_key=True, serialize=False),
                ),
                ("correo", models.EmailField(max_length=200, unique=True)),
                ("telefono", models.CharField(max_length=10)),
                ("clave", models.CharField(max_length=128)),
                (
                    "estado",
                    models.CharField(
                        choices=[("A", "Activo"), ("I", "Inactivo")],
                        default="A",
                        max_length=1,
                    ),
                ),
                ("fecha_registro", models.DateTimeField(auto_now_add=True)),
                (
                    "id_rol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.roles"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UsuarioEmpresa",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.usuario",
                    ),
                ),
                ("id_empresa", models.CharField(max_length=13, unique=True)),
                ("razon_social", models.CharField(max_length=200)),
                ("actividad_comercial", models.CharField(max_length=200)),
                ("ced_rep_legal", models.CharField(max_length=10)),
                ("nom_rep_legal", models.CharField(max_length=200)),
                ("direccion", models.CharField(max_length=200)),
                ("redes", models.CharField(max_length=1000)),
            ],
            bases=("api.usuario",),
        ),
        migrations.CreateModel(
            name="UsuarioPersona",
            fields=[
                (
                    "usuario_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.usuario",
                    ),
                ),
                ("id_persona", models.CharField(max_length=13, unique=True)),
                ("nombres", models.CharField(max_length=100)),
                ("apellidos", models.CharField(max_length=100)),
                ("provincia", models.CharField(max_length=100)),
                ("ciudad", models.CharField(max_length=100)),
                ("direccion", models.CharField(max_length=200)),
                ("fec_nac", models.DateField()),
                (
                    "genero",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Femenino")], max_length=1
                    ),
                ),
            ],
            bases=("api.usuario",),
        ),
        migrations.CreateModel(
            name="SolicitudRecoleccion",
            fields=[
                (
                    "id_solicitud",
                    models.CharField(max_length=13, primary_key=True, serialize=False),
                ),
                ("id_reciclador", models.CharField(max_length=13)),
                ("descripcion", models.CharField(max_length=1000)),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("P", "Pendiente"),
                            ("A", "Aceptada"),
                            ("C", "Cancelada"),
                            ("F", "Fallida"),
                            ("E", "Entregada"),
                        ],
                        max_length=1,
                    ),
                ),
                ("fecha_inicio", models.DateTimeField(auto_now_add=True)),
                ("fecha_asig", models.DateTimeField(blank=True, null=True)),
                ("fecha_fin", models.DateTimeField(blank=True, null=True)),
                (
                    "id_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.usuario"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReporteDenuncias",
            fields=[
                ("id_reporte", models.AutoField(primary_key=True, serialize=False)),
                ("descripcion", models.CharField(max_length=1000)),
                (
                    "estado",
                    models.CharField(
                        choices=[("A", "Activo"), ("I", "Inactivo")], max_length=1
                    ),
                ),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "resolucion",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "id_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="denuncias_realizadas",
                        to="api.usuario",
                    ),
                ),
                (
                    "id_usuario_rep",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="denuncias_recibidas",
                        to="api.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ArchivosSolicitudes",
            fields=[
                (
                    "id_archivo_solicitud",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "archivo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.archivo"
                    ),
                ),
                (
                    "solicitud",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.solicitudrecoleccion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ArchivosReportes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_archivo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.archivo"
                    ),
                ),
                (
                    "id_reporte",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.reportedenuncias",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reciclador",
            fields=[
                (
                    "usuariopersona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="api.usuariopersona",
                    ),
                ),
                ("id_reciclador", models.CharField(max_length=13, unique=True)),
                ("id_empresa", models.CharField(max_length=13, unique=True)),
                ("calificacion_reciclador", models.IntegerField()),
                ("nacionalidad", models.CharField(max_length=100)),
                (
                    "estado_reciclador",
                    models.CharField(
                        choices=[("A", "Activo"), ("I", "Inactivo")],
                        default="A",
                        max_length=1,
                    ),
                ),
            ],
            bases=("api.usuariopersona",),
        ),
        migrations.CreateModel(
            name="RelacionEmpresa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_emp_hijo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="empresa_hija",
                        to="api.usuarioempresa",
                    ),
                ),
                (
                    "id_empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="empresa_padre",
                        to="api.usuarioempresa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarnetRecolectores",
            fields=[
                (
                    "id_archivo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="api.archivo",
                    ),
                ),
                (
                    "id_recolector",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="api.reciclador"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Calificacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("calificacion_reciclador", models.IntegerField()),
                ("observacion", models.CharField(max_length=1000)),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "id_usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.usuariopersona",
                    ),
                ),
                (
                    "id_reciclador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="calificaciones_reciclador",
                        to="api.reciclador",
                    ),
                ),
            ],
        ),
    ]
