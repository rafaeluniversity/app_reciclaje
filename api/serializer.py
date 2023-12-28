from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .models import Roles, Usuario, RolesUsuarios, UsuarioEmpresa, UsuarioPersona, Recolector, Calificaciones, SolicitudRecoleccion, Archivos, CarnetRecolector, ArchivosSolicitudes, ReportesDenuncias, ArchivosReportes, RelacionEmpresa

class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    tipo_usuario = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = get_user_model().objects.filter(email=email).first()

        if user and user.check_password(password):
            data['tipo_usuario'] = user.tipo_usuario
        else:
            raise serializers.ValidationError('Credenciales inválidas')

        return data

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RolesUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesUsuarios
        fields = '__all__'

class UsuarioEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEmpresa
        fields = '__all__'

class UsuarioPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersona
        fields = '__all__'

class RecolectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recolector
        fields = '__all__'

class CalificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificaciones
        fields = '__all__'

class SolicitudRecoleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudRecoleccion
        fields = '__all__'

class ArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos
        fields = '__all__'

class CarnetRecolectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarnetRecolector
        fields = '__all__'

class ArchivosSolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivosSolicitudes
        fields = '__all__'

class ReportesDenunciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportesDenuncias
        fields = '__all__'

class ArchivosReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivosReportes
        fields = '__all__'

class RelacionEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionEmpresa
        fields = '__all__'