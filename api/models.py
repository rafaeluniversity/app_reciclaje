from django.db import models
from django.db.models import JSONField
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Imagen(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/')

    def get_image_url(self):
        return self.imagen.url

    def __str__(self):
        return f"ID: {self.id_imagen}, URL: {self.get_image_url()}"

class Roles(models.Model):
    id_rol = models.CharField(primary_key=True, max_length=13, unique=True)
    descripcion = models.CharField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Genera automáticamente el id_rol como 'rol_001', 'rol_002', etc.
        if not self.id_rol:
            last_id = Roles.objects.all().order_by('-id_rol').first()
            new_id = 1 if not last_id else int(last_id.id_rol.split('_')[1]) + 1
            self.id_rol = 'rol_{:03d}'.format(new_id)

        # Llama al método save de la clase base para guardar el objeto
        super(Roles, self).save(*args, **kwargs)

    def __str__(self):
        return self.id_rol

class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=13)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=200, unique=True)
    telefono = models.CharField(max_length=10)
    clave = models.CharField(max_length=128)
    ESTADO_CHOICES = [('A', 'Activo'), ('I', 'Inactivo')]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    url_foto = models.URLField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Genera automáticamente el id_usuario como 'user_001', 'user_002', etc.
        if not self.id_usuario:
            last_id = Usuario.objects.all().order_by('-id_usuario').first()
            new_id = 1 if not last_id else int(last_id.id_usuario.split('_')[1]) + 1
            self.id_usuario = 'user_{:03d}'.format(new_id)

        # Llama al método save de la clase base para guardar el objeto
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.id_usuario

class UsuarioPersona(Usuario):
    id_persona = models.CharField(unique=True, max_length=13)
    cedula = models.CharField(unique=True, max_length=13)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fec_nac = models.DateField()
    GENERO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino')]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)

    def save(self, *args, **kwargs):
        # Genera automáticamente el id_persona como 'per_001', 'per_002', etc.
        if not self.id_persona:
            last_id = UsuarioPersona.objects.all().order_by('-id_persona').first()
            new_id = 1 if not last_id else int(last_id.id_persona.split('_')[1]) + 1
            self.id_persona = 'per_{:03d}'.format(new_id)

        # Llama al método save de la clase base para guardar el objeto
        super(UsuarioPersona, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class UsuarioEmpresa(Usuario):
    id_empresa = models.CharField(max_length=13, unique=True)
    razon_social = models.CharField(max_length=200)
    actividad_comercial = models.CharField(max_length=200)
    ced_rep_legal = models.CharField(max_length=10)
    nom_rep_legal = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    redes = JSONField(default=dict)  # Cambiar a JSONField para almacenar datos JSON
    ruc = models.CharField(max_length=13, unique=True)  # Nuevo campo para el RUC

    def save(self, *args, **kwargs):
        # Lógica de generación de id_empresa si es necesario
        if not self.id_empresa:
            last_id = UsuarioEmpresa.objects.all().order_by('-id_empresa').first()
            new_id = 1 if not last_id else int(last_id.id_empresa.split('_')[1]) + 1
            self.id_empresa = 'emp_{:03d}'.format(new_id)

        # Llama al método save de la clase base para guardar el objeto
        super(UsuarioEmpresa, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.razon_social} ({self.ruc})"

class RelacionEmpresa(models.Model):
    id_empresa = models.ForeignKey(UsuarioEmpresa, on_delete=models.CASCADE, related_name='empresa_padre')
    id_emp_hijo = models.ForeignKey(UsuarioEmpresa, on_delete=models.CASCADE, related_name='empresa_hija')

    def __str__(self):
        return f'Relación {self.id_empresa} - {self.id_emp_hijo}'

class Reciclador(UsuarioPersona):
    id_reciclador = models.CharField(unique=True, max_length=13)
    id_empresa = models.CharField(max_length=13)
    calificacion_reciclador = models.IntegerField()
    nacionalidad = models.CharField(max_length=100)

    ESTADO_CHOICES = [('A', 'Activo'), ('I', 'Inactivo'), ('E', 'Espera')]
    estado_reciclador = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='E')

    def save(self, *args, **kwargs):
        if not self.id_reciclador:
            last_id = Reciclador.objects.all().order_by('-id_reciclador').first()
            new_id = 1 if not last_id else int(last_id.id_reciclador.split('_')[1]) + 1
            self.id_reciclador = 'rec_{:03d}'.format(new_id)

        super(Reciclador, self).save(*args, **kwargs)

    def __str__(self):
        return f"Reciclador {self.id_reciclador} - {self.nacionalidad} ({self.estado})"

class Archivo(models.Model):
    id_archivo = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    url = models.TextField()

    def __str__(self):
        return f"Archivo {self.id_archivo} - {self.descripcion} ({self.fecha_subida})"


class CarnetRecolectores(models.Model):
    id_archivo = models.OneToOneField(Archivo, primary_key=True, on_delete=models.CASCADE)
    id_recolector = models.OneToOneField(Reciclador, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carnet de Recolector {self.id_recolector} - Archivo {self.id_archivo}"

class SolicitudRecoleccion(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),#solicitud en curso
        ('A', 'Aceptada'),#solicitud en curso
        ('L', 'Cerca'),#solicitud en curso
        ('R', 'Recolectada'),#solicitud en curso
        ('CR', 'Cancelada Reciclador'),#solicitud en curso solo para solicitante, cuando este acepte se cambia el estado a FC
        ('CU', 'Cancelada Usuario'),#solicitud en curso solo para reciclador, cuando este acepte se cambia el estado a FC
        ('FC', 'Fin Cancelada'),
        ('F', 'Fin')
    ]

    id_solicitud = models.CharField(primary_key=True, max_length=13)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_reciclador = models.CharField(max_length=13)
    descripcion = models.CharField(max_length=1000)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_asig = models.DateTimeField(null=True, blank=True)
    fecha_arribo = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Genera automáticamente el id_solicitud como 'sol_001', 'sol_002', etc.
        if not self.id_solicitud:
            last_id = SolicitudRecoleccion.objects.all().order_by('-id_solicitud').first()
            new_id = 1 if not last_id else int(last_id.id_solicitud.split('_')[1]) + 1
            self.id_solicitud = 'sol_{:03d}'.format(new_id)

        # Llama al método save de la clase base para guardar el objeto
        super(SolicitudRecoleccion, self).save(*args, **kwargs)

    def __str__(self):
        return f"Solicitud {self.id_solicitud} - Estado: {self.get_estado_display()}"

class SolicitudDetalle(models.Model):
    id_solicitud = models.OneToOneField(SolicitudRecoleccion, on_delete=models.CASCADE, primary_key=True)
    materiales = models.TextField(help_text="Lista de materiales separados por comas")
    direccion = models.CharField(max_length=255, help_text="Dirección del solicitante")
    ubicacion = models.JSONField(help_text="Ubicación como lista [latitud, longitud]")
    ubicacion_reciclador = models.JSONField(help_text="Ubicación del reciclador como lista [latitud, longitud]", null=True, blank=True)
    calificado = models.BooleanField(default=False)
    fotos = models.ManyToManyField(Imagen, related_name='solicitudes', blank=True)

    def __str__(self):
        return f"SolicitudDetalle {self.id_solicitud_id}"

    def save(self, *args, **kwargs):
        # Validar que los materiales existan en el modelo TipoMaterial
        lista_materiales = self.materiales.split(', ')

        materiales_validos = TipoMaterial.objects.filter(descripcion__in=lista_materiales).count()

        print(materiales_validos)
        '''
        if materiales_validos != len(lista_materiales):
            raise ValidationError("Uno o más materiales no son válidos.")
        '''
        super(SolicitudDetalle, self).save(*args, **kwargs)

class ArchivosSolicitudes(models.Model):
    id_archivo_solicitud = models.BigAutoField(primary_key=True)
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(SolicitudRecoleccion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Archivo_Solicitud {self.id_archivo_solicitud} - Solicitud: {self.solicitud.id_solicitud}"

'''
class Calificacion(models.Model):
    id_reciclador = models.ForeignKey(Reciclador, on_delete=models.CASCADE, related_name='calificaciones_reciclador')
    id_usuario = models.ForeignKey(UsuarioPersona, on_delete=models.CASCADE)
    calificacion_reciclador = models.IntegerField()
    observacion = models.CharField(max_length=1000)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calificacion {self.id} - Reciclador: {self.id_reciclador} - Usuario: {self.id_usuario}"
'''

class Calificacion(models.Model):
    id_usuario_calificador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_calificador')
    id_usuario_calificado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_calificado')
    id_solicitud = models.ForeignKey(SolicitudRecoleccion, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calificacion {self.id} - Usuario calificador: {self.id_usuario_calificador} - Usuario calificado: {self.id_usuario_calificado}"

class SolicitudesCanceladas(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_cancela')
    id_solicitud = models.ForeignKey(SolicitudRecoleccion, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cancelacion {self.id}"


class ReporteDenuncias(models.Model):
    ESTADO_CHOICES = [('A', 'Activo'), ('I', 'Inactivo')]

    id_reporte = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='denuncias_realizadas')
    id_usuario_rep = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='denuncias_recibidas')
    descripcion = models.CharField(max_length=1000)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)
    resolucion = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"Reporte {self.id_reporte} - {self.id_usuario} -> {self.id_usuario_rep}"

class ArchivosReportes(models.Model):
    id_archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    id_reporte = models.ForeignKey(ReporteDenuncias, on_delete=models.CASCADE)

    def __str__(self):
        return f"Archivo-Reporte {self.id_archivo} - {self.id_reporte}"

class Territorio(models.Model):
    id_territorio = models.IntegerField(primary_key=True)
    id_nivel_territorial = models.IntegerField()
    id_territorio_padre = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)

    class Meta:
        db_table = 'urm_territorios'

class TipoMaterial(models.Model):
    id_tipo_material = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    ESTADO_CHOICES = [('A', 'Activo'), ('I', 'Inactivo')]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self):
        return f"TipoMaterial {self.id_tipo_material} - Descripción: {self.descripcion}, Estado: {self.estado}"

class RegistroReciclaje(models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_reciclador = models.ForeignKey(Reciclador, on_delete=models.CASCADE)
    id_material = models.ForeignKey(TipoMaterial, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario_ingreso = models.ForeignKey(Usuario, related_name='usuario_ingreso', on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    id_usuario_modificacion = models.ForeignKey(Usuario, related_name='usuario_modificacion', on_delete=models.CASCADE,default="")
    ESTADO_CHOICES = [('A', 'Activo'), ('I', 'Inactivo')]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='A')

    def __str__(self):
        return f"RegistroReciclaje {self.id_registro} - Reciclador: {self.id_reciclador}, Material: {self.id_material}, Peso: {self.peso}kg, Estado: {self.estado}"

#---------------------
#modelos para el inicio

class CarruselFoto(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    imageURL = models.URLField(max_length=200)
    orden = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('A', 'Activo'), ('I', 'Inactivo')])

    def __str__(self):
        return f"{self.title} - Orden: {self.orden}"

class QuienesSomos(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=350)
    imageURL = models.URLField(max_length=200)
    orden = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('A', 'Activo'), ('I', 'Inactivo')])

    def __str__(self):
        return f"{self.title} - Orden: {self.orden}"

class Seccion(models.Model):
    title = models.CharField(max_length=50)
    imageURL = models.URLField(max_length=200, null=True, blank=True)
    orden = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('A', 'Activo'), ('I', 'Inactivo')])

    def __str__(self):
        return self.title

class Parrafo(models.Model):
    seccion = models.ForeignKey(Seccion, related_name='parrafos', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    imageURL = models.URLField(max_length=200, null=True, blank=True)
    orden = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('A', 'Activo'), ('I', 'Inactivo')])

    def __str__(self):
        return f"{self.title} - Sección: {self.seccion.title}"

class Timeline(models.Model):
    seccion = models.ForeignKey(Seccion, related_name='timelines', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    orden = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('A', 'Activo'), ('I', 'Inactivo')])

    def __str__(self):
        return f"{self.title} - Sección: {self.seccion.title}"

class PasosTimeline(models.Model):
    timeline = models.ForeignKey(Timeline, related_name='pasos', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    numero = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('A', 'Activo'), ('I', 'Inactivo')])

    def __str__(self):
        return f"{self.title} - Timeline: {self.timeline.title}"

    def clean(self):
        # Validar que el número de paso sea único dentro del mismo timeline
        if PasosTimeline.objects.filter(timeline=self.timeline, numero=self.numero).exists():
            raise ValidationError({'numero': 'El número de paso debe ser único dentro del timeline.'})

class CentroAcopio(models.Model):
    id_centro = models.AutoField(primary_key=True)  # Define id_centro como clave primaria
    organizacion = models.ForeignKey('UsuarioEmpresa', related_name='centros_acopio', on_delete=models.CASCADE)
    nombre_acopio = models.CharField(max_length=100)
    ubicacion = models.JSONField(help_text="Ubicación como lista [latitud, longitud]")
    referencia = models.TextField()
    estado = models.CharField(max_length=10, choices=[('A', 'Activo'), ('I', 'Inactivo')])
    informacion = models.CharField(max_length=250, blank=True, null=True, help_text="Información adicional sobre el centro de acopio")
    fotos = models.ManyToManyField(Imagen, related_name='centros_acopio_imagen', blank=True)

    def __str__(self):
        return f"{self.nombre_acopio} - {self.organizacion.razon_social}"

    def save(self, *args, **kwargs):
        # Validar antes de guardar
        super().save(*args, **kwargs)

class SolicitudRechazada(models.Model):
    id_solicitud = models.ForeignKey('SolicitudRecoleccion', on_delete=models.CASCADE, related_name='rechazos')
    id_reciclador = models.ForeignKey('Reciclador', on_delete=models.CASCADE, related_name='rechazos_realizados')
    fecha_rechazo = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Rechazo de Solicitud {self.id_solicitud_id} por Reciclador {self.id_reciclador_id} el {self.fecha_rechazo.strftime('%Y-%m-%d %H:%M:%S')}"

class UsuarioTemporal(models.Model):
    correo = models.EmailField(max_length=200, unique=True)
    clave = models.CharField(max_length=128)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    email_verification_token = models.CharField(max_length=100, blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    tipo_usuario = models.CharField(max_length=10, choices=[('empresa', 'Empresa'), ('persona', 'Persona'), ('reciclador', 'Reciclador')])
    datos_adicionales = JSONField(default=dict, blank=True, null=True)  # Usar JSONField para datos adicionales

    def __str__(self):
        return self.correo
