from rest_framework import serializers
from .models import (
    Roles, Usuario, UsuarioPersona, UsuarioEmpresa,
    RelacionEmpresa, Reciclador, Calificacion, Archivo,
    CarnetRecolectores, SolicitudRecoleccion, ArchivosSolicitudes,
    ReporteDenuncias, ArchivosReportes, Imagen)

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
