from rest_framework import viewsets
from django.http import JsonResponse
from django.db import connection
from .models import Usuario
import json
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt

from .serializer import (
    RolesSerializer, UsuarioSerializer, RolesUsuariosSerializer,
    UsuarioEmpresaSerializer, UsuarioPersonaSerializer, RecolectorSerializer,
    CalificacionesSerializer, SolicitudRecoleccionSerializer, ArchivosSerializer,
    CarnetRecolectorSerializer, ArchivosSolicitudesSerializer, ReportesDenunciasSerializer,
    ArchivosReportesSerializer, RelacionEmpresaSerializer
)
from .models import (
    Roles, Usuario, RolesUsuarios, UsuarioEmpresa, UsuarioPersona, Recolector,
    Calificaciones, SolicitudRecoleccion, Archivos, CarnetRecolector,
    ArchivosSolicitudes, ReportesDenuncias, ArchivosReportes, RelacionEmpresa
)


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RolesUsuariosViewSet(viewsets.ModelViewSet):
    queryset = RolesUsuarios.objects.all()
    serializer_class = RolesUsuariosSerializer

class UsuarioEmpresaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioEmpresa.objects.all()
    serializer_class = UsuarioEmpresaSerializer

class UsuarioPersonaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPersona.objects.all()
    serializer_class = UsuarioPersonaSerializer

class RecolectorViewSet(viewsets.ModelViewSet):
    queryset = Recolector.objects.all()
    serializer_class = RecolectorSerializer

class CalificacionesViewSet(viewsets.ModelViewSet):
    queryset = Calificaciones.objects.all()
    serializer_class = CalificacionesSerializer

class SolicitudRecoleccionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudRecoleccion.objects.all()
    serializer_class = SolicitudRecoleccionSerializer

class ArchivosViewSet(viewsets.ModelViewSet):
    queryset = Archivos.objects.all()
    serializer_class = ArchivosSerializer

class CarnetRecolectorViewSet(viewsets.ModelViewSet):
    queryset = CarnetRecolector.objects.all()
    serializer_class = CarnetRecolectorSerializer

class ArchivosSolicitudesViewSet(viewsets.ModelViewSet):
    queryset = ArchivosSolicitudes.objects.all()
    serializer_class = ArchivosSolicitudesSerializer

class ReportesDenunciasViewSet(viewsets.ModelViewSet):
    queryset = ReportesDenuncias.objects.all()
    serializer_class = ReportesDenunciasSerializer

class ArchivosReportesViewSet(viewsets.ModelViewSet):
    queryset = ArchivosReportes.objects.all()
    serializer_class = ArchivosReportesSerializer

class RelacionEmpresaViewSet(viewsets.ModelViewSet):
    queryset = RelacionEmpresa.objects.all()
    serializer_class = RelacionEmpresaSerializer

def login_view(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            
            email = body_data.get("email")
            password = body_data.get("password")

            # Filtrar usuarios por el correo electrónico
            user = Usuario.objects.filter(email=email).first()

            if user and user.password == password:
                # Las contraseñas coinciden
                # Puedes incluir cualquier otro dato del usuario que desees enviar
                user_data = {
                    "id": user.id_usuario,
                    "email": user.email,
                    "tipo_usuario": user.tipo_usuario,
                    # Agrega más campos según sea necesario
                }
                response = JsonResponse({"success": True, "user_data": user_data})

                # Configura las cookies adecuadamente
                response.set_cookie("user_data", json.dumps(user_data))
                
                return response
            else:
                # Las contraseñas no coinciden o el usuario no existe
                return JsonResponse({"error": "Credenciales incorrectas"}, status=400)

        else:
            return JsonResponse({"error": "Método no permitido"}, status=405)

    except Exception as e:
        # Imprime detalles de la excepción
        print(f"Error en la vista de login: {str(e)}")
        
        # Devuelve un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500)
    
    
def logout_view(request):
    response = JsonResponse({"success": True})
    
    # Elimina la cookie user_data
    response.delete_cookie('user_data')
    
    return response

def check_database_connection(request):
    try:
        # Intenta realizar una consulta simple para comprobar la conexión
        with connection.cursor():
            pass
        return JsonResponse({'connected': True})
    except Exception as e:
        return JsonResponse({'connected': False, 'error': str(e)})