from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Roles(models.Model):
    id_rol = models.CharField(primary_key=True, max_length=13)
    descripcion = models.CharField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class Usuario(AbstractUser):
    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]

    TIPO_USUARIO_CHOICES = [
        ('persona', 'Persona'),
        ('recolector', 'Recolector'),
        ('empresa', 'Empresa'),
    ]

    id_usuario = models.CharField(primary_key=True, max_length=13)
    correo = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.DateTimeField(auto_now_add=True)
    username = models.CharField(
        max_length=30,
        unique=True,
        default='',  # Puedes ajustar el valor predeterminado según tus necesidades
    )
    password = models.CharField(max_length=128, default='default_password_hash')

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        default='A'
    )
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        default='persona'
    )

    # Agregar el argumento related_name a los campos groups y user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuarios_groups',  # Cambiar a un nombre que prefieras
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuarios_user_permissions',  # Cambiar a un nombre que prefieras
    )

class RolesUsuarios(models.Model):
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class UsuarioEmpresa(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=200)
    actividad_comercial = models.CharField(max_length=200)
    ced_rep_legal = models.CharField(max_length=10)
    nom_rep_legal = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    redes = models.CharField(max_length=1000)


class UsuarioPersona(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField()

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    genero = models.CharField(
        max_length=1,
        choices=GENERO_CHOICES
    )


class Recolector(models.Model):
    id_usuario_p = models.ForeignKey(UsuarioPersona, on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(UsuarioEmpresa, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    nacionalidad = models.CharField(max_length=100)

    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES
    )


class Calificaciones(models.Model):
    id_recolector = models.ForeignKey(Recolector, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    observacion = models.CharField(max_length=1000)
    fecha = models.DateTimeField()


class SolicitudRecoleccion(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_recolector = models.ForeignKey(Recolector, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=1000)

    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('A', 'Aceptada'),
        ('C', 'Cancelada'),
        ('F', 'Finalizada'),
        ('E', 'En proceso'),
    ]
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES
    )

    fecha_inicio = models.DateTimeField()
    fecha_asig = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)


class Archivos(models.Model):
    id_archivo = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    url = models.TextField()


class CarnetRecolector(models.Model):
    id_archivo = models.ForeignKey(Archivos, on_delete=models.CASCADE)
    id_recolector = models.ForeignKey(Recolector, on_delete=models.CASCADE)


class ArchivosSolicitudes(models.Model):
    id_archivo = models.ForeignKey(Archivos, on_delete=models.CASCADE)
    id_solicitud = models.ForeignKey(
        SolicitudRecoleccion, on_delete=models.CASCADE)


class ReportesDenuncias(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_usuario_rep = models.ForeignKey(
        Usuario, related_name='usuario_reportado', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=1000)

    ESTADO_CHOICES = [
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES
    )

    fecha = models.DateTimeField(auto_now_add=True)
    resolucion = models.CharField(max_length=1000)


class ArchivosReportes(models.Model):
    id_archivo = models.ForeignKey(Archivos, on_delete=models.CASCADE)
    id_reporte = models.ForeignKey(ReportesDenuncias, on_delete=models.CASCADE)


class RelacionEmpresa(models.Model):
    id_empresa = models.ForeignKey(
        UsuarioEmpresa, related_name='empresa_padre', on_delete=models.CASCADE)
    id_emp_hijo = models.ForeignKey(
        UsuarioEmpresa, related_name='empresa_hijo', on_delete=models.CASCADE)
