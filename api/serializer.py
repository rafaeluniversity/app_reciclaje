from rest_framework import serializers
from .models import (
    Roles, Usuario, UsuarioPersona, UsuarioEmpresa,
    RelacionEmpresa, Reciclador, Calificacion, Archivo,
    CarnetRecolectores, SolicitudRecoleccion, ArchivosSolicitudes,
    ReporteDenuncias, ArchivosReportes, Imagen,
    CarruselFoto, QuienesSomos, Seccion,
    Parrafo, Timeline, PasosTimeline,
    CentroAcopio, SolicitudDetalle, TipoMaterial,
    SolicitudesCanceladas)

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ('id_imagen', 'imagen', 'get_image_url')

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersona
        fields = '__all__'

class UsuarioEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEmpresa
        fields = '__all__'

class RelacionEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionEmpresa
        fields = '__all__'

class RecicladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciclador
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = '__all__'

class CarnetRecolectoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarnetRecolectores
        fields = '__all__'

class SolicitudRecoleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudRecoleccion
        fields = '__all__'

class ArchivosSolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivosSolicitudes
        fields = '__all__'

class ReporteDenunciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteDenuncias
        fields = '__all__'

class ArchivosReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivosReportes
        fields = '__all__'

class CarruselFotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarruselFoto
        fields = '__all__'

class QuienesSomosSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class ParrafoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parrafo
        fields = '__all__'

class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = '__all__'

class PasosTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasosTimeline
        fields = '__all__'

class CentroAcopioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroAcopio
        fields = '__all__'

class SolicitudesCanceladasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudesCanceladas
        fields = '__all__'

class SolicitudDetalleSerializer(serializers.ModelSerializer):
    fotos = ImagenSerializer(many=True, read_only=True)

    class Meta:
        model = SolicitudDetalle
        fields = ('id_solicitud', 'materiales', 'direccion', 'ubicacion', 'calificado', 'fotos')

class CrearSolicitudSerializer(serializers.Serializer):
    materiales = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False
    )
    direccion = serializers.CharField(max_length=255)
    ubicacion = serializers.ListField(
        child=serializers.FloatField(),
        allow_empty=False,
        min_length=2,
        max_length=2
    )
    fotos = serializers.ListField(
        child=serializers.ImageField(),
        required=False
    )

    def validate_materiales(self, value):
        if not all(TipoMaterial.objects.filter(descripcion=material).exists() for material in value):
            raise serializers.ValidationError("Algunos materiales no son válidos.")
        return value
