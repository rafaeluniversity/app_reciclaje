from rest_framework import viewsets
from django.db import models
from django.http import JsonResponse
from django.db import transaction, connection
import json
from django.contrib.auth.hashers import check_password, make_password, is_password_usable
from datetime import datetime

from .serializer import (
    RolesSerializer,
    UsuarioSerializer,
    UsuarioPersonaSerializer,
    UsuarioEmpresaSerializer,
    RelacionEmpresaSerializer,
    RecicladorSerializer,
    CalificacionSerializer,
    ArchivoSerializer,
    CarnetRecolectoresSerializer,
    SolicitudRecoleccionSerializer,
    ArchivosSolicitudesSerializer,
    ReporteDenunciasSerializer,
    ArchivosReportesSerializer
)

from .models import (
    Roles,
    Usuario,
    UsuarioPersona,
    UsuarioEmpresa,
    RelacionEmpresa,
    Reciclador,
    Calificacion,
    Archivo,
    CarnetRecolectores,
    SolicitudRecoleccion,
    ArchivosSolicitudes,
    ReporteDenuncias,
    ArchivosReportes
)


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioPersonaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPersona.objects.all()
    serializer_class = UsuarioPersonaSerializer

class UsuarioEmpresaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioEmpresa.objects.all()
    serializer_class = UsuarioEmpresaSerializer

class RelacionEmpresaViewSet(viewsets.ModelViewSet):
    queryset = RelacionEmpresa.objects.all()
    serializer_class = RelacionEmpresaSerializer

class RecicladorViewSet(viewsets.ModelViewSet):
    queryset = Reciclador.objects.all()
    serializer_class = RecicladorSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

class CarnetRecolectoresViewSet(viewsets.ModelViewSet):
    queryset = CarnetRecolectores.objects.all()
    serializer_class = CarnetRecolectoresSerializer

class SolicitudRecoleccionViewSet(viewsets.ModelViewSet):
    queryset = SolicitudRecoleccion.objects.all()
    serializer_class = SolicitudRecoleccionSerializer

class ArchivosSolicitudesViewSet(viewsets.ModelViewSet):
    queryset = ArchivosSolicitudes.objects.all()
    serializer_class = ArchivosSolicitudesSerializer

class ReporteDenunciasViewSet(viewsets.ModelViewSet):
    queryset = ReporteDenuncias.objects.all()
    serializer_class = ReporteDenunciasSerializer

class ArchivosReportesViewSet(viewsets.ModelViewSet):
    queryset = ArchivosReportes.objects.all()
    serializer_class = ArchivosReportesSerializer

#Registro de un usuario de tipo empresa
def registroEmpresa(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Extraer datos del cuerpo de la solicitud
            correo = body_data.get("correo")
            clave = body_data.get("clave")
            razon_social = body_data.get("razon_social")
            actividad_comercial = body_data.get("actividad_comercial")
            ced_rep_legal = body_data.get("ced_rep_legal")
            nom_rep_legal = body_data.get("nom_rep_legal")
            direccion = body_data.get("direccion")
            redes = body_data.get("redes")

            # Verificar la unicidad del correo electrónico y la razón social
            if UsuarioEmpresa.objects.filter(correo=correo).exists():
                return JsonResponse({"error": "El correo electrónico ya está en uso"}, status=400, charset='utf-8')

            if UsuarioEmpresa.objects.filter(razon_social=razon_social).exists():
                return JsonResponse({"error": "La razón social ya está en uso"}, status=400, charset='utf-8')
            
            print(make_password(clave))

            # Crear un nuevo objeto UsuarioEmpresa
            usuario_empresa = UsuarioEmpresa(
                correo=correo,
                clave=make_password(clave),
                razon_social=razon_social,
                actividad_comercial=actividad_comercial,
                ced_rep_legal=ced_rep_legal,
                nom_rep_legal=nom_rep_legal,
                direccion=direccion,
                redes=redes,
                id_rol=Roles.objects.get(id_rol='rol_002')  # Asignar el rol correspondiente
            )

            # Guardar el objeto en la base de datos
            usuario_empresa.save()

            return JsonResponse({"success": True, "message": "UsuarioEmpresa registrado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error en registroEmpresa: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500, charset='utf-8')

#
def registroPersona(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Extraer datos del cuerpo de la solicitud
            correo = body_data.get("correo")
            clave = body_data.get("clave")
            nombres = body_data.get("nombres")
            apellidos = body_data.get("apellidos")
            provincia = body_data.get("provincia")
            ciudad = body_data.get("ciudad")
            direccion = body_data.get("direccion")
            edad = body_data.get("edad")
            genero = body_data.get("genero")

            # Verificar la unicidad del correo electrónico
            if UsuarioPersona.objects.filter(correo=correo).exists():
                return JsonResponse({"error": "El correo electrónico ya está en uso"}, status=400, charset='utf-8')

            # Crear un nuevo objeto UsuarioPersona
            usuario_persona = UsuarioPersona(
                correo=correo,
                clave=make_password(clave),
                nombres=nombres,
                apellidos=apellidos,
                provincia=provincia,
                ciudad=ciudad,
                direccion=direccion,
                edad=edad,
                genero=genero,
                id_rol=Roles.objects.get(id_rol='rol_004')  # Asignar el rol correspondiente
            )

            # Guardar el objeto en la base de datos
            usuario_persona.save()

            return JsonResponse({"success": True, "message": "UsuarioPersona registrado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error en registroPersona: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500, charset='utf-8')

#
def registroReciclador(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Extraer datos del cuerpo de la solicitud
            id_empresa = body_data.get("id_empresa")
            calificacion = body_data.get("calificacion")
            nacionalidad = body_data.get("nacionalidad")
            correo = body_data.get("correo")
            clave = body_data.get("clave")

            # Verificar la unicidad del correo electrónico
            if Usuario.objects.filter(correo=correo).exists():
                return JsonResponse({"error": "El correo electrónico ya está en uso"}, status=400, charset='utf-8')

            # Crear un nuevo objeto Usuario
            usuario = Usuario(
                correo=correo,
                clave=make_password(clave),
                id_rol=Roles.objects.get(id_rol='rol_003')  # Asignar el rol correspondiente
            )

            # Guardar el objeto Usuario en la base de datos
            usuario.save()


            # Crear un nuevo objeto Reciclador asociado al usuario creado y a la empresa
            reciclador = Reciclador(
                calificacion=calificacion,
                nacionalidad=nacionalidad,
                id_empresa=id_empresa
            )

            # Guardar el objeto Reciclador en la base de datos
            reciclador.save()

            return JsonResponse({"success": True, "message": "Reciclador registrado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error en registroReciclador: {str(e)}")
        usuario.delete()
        #transaction.set_rollback(True)

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500, charset='utf-8')
    
#
def login_view(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            correo = body_data.get("correo")
            clave = body_data.get("clave")

            # Filtrar usuarios por el correo electrónico
            user = Usuario.objects.filter(correo=correo).first()


            if user and check_password(clave, user.clave):
                # Las contraseñas coinciden
                user_data = {
                    "id_usuario": user.id_usuario,
                    "rol": user.id_rol.descripcion,
                    # Agrega más campos según sea necesario
                }

                return JsonResponse({"success": True, "user_data": user_data})
            else:
                # Las credenciales no coinciden o el usuario no existe
                return JsonResponse({"error": "Credenciales incorrectas"}, status=400)
        else:
            return JsonResponse({"error": "Método no permitido"}, status=405)

    except Exception as e:
        # Utiliza el sistema de registro de Django para manejar errores
        # logging.error(f"Error en la vista de login: {str(e)}")
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500)

#
def generar_solicitud(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            id_usuario = body_data.get("id_usuario")
            #id_reciclador = body_data.get("id_reciclador")
            descripcion = body_data.get("descripcion")

            # Verificar que el usuario y el reciclador existan
            usuario = Usuario.objects.get(id_usuario=id_usuario)
            #reciclador = Reciclador.objects.get(id_reciclador=id_reciclador)

            # Crear una nueva solicitud con el estado por defecto como "Pendiente"
            solicitud = SolicitudRecoleccion(
                id_usuario=usuario,
                descripcion=descripcion,
                estado='P'  # 'P' representa "Pendiente"
            )

            # Guardar la solicitud en la base de datos
            solicitud.save()

            return JsonResponse({"success": True, "message": "Solicitud generada exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except Usuario.DoesNotExist:
        return JsonResponse({"error": "El usuario no existe"}, status=400, charset='utf-8')

    except Reciclador.DoesNotExist:
        return JsonResponse({"error": "El reciclador no existe"}, status=400, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al generar solicitud: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500, charset='utf-8')


def actualizar_solicitud(request):
    try:
        # Verificar que la solicitud sea de tipo POST
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Obtener el id_solicitud y id_reciclador del cuerpo de la solicitud JSON
            id_solicitud = body_data.get("id_solicitud")
            id_reciclador = body_data.get("id_reciclador")

            # Obtener la solicitud existente por su id_solicitud
            solicitud = SolicitudRecoleccion.objects.get(id_solicitud=id_solicitud)

            # Actualizar los campos id_reciclador y estado
            solicitud.id_reciclador = id_reciclador
            solicitud.estado = 'A'  # 'A' representa "Aceptada"

            # Actualizar la fecha_asig con la fecha y hora actuales
            solicitud.fecha_asig = datetime.now()

            # Guardar los cambios en la base de datos
            solicitud.save()

            return JsonResponse({"success": True, "message": f"Solicitud {id_solicitud} actualizada exitosamente"}, charset='utf-8')

        else:
            # Devolver un error si el método de solicitud no es POST
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except SolicitudRecoleccion.DoesNotExist:
        # Devolver un error si la solicitud no existe
        return JsonResponse({"error": "La solicitud no existe"}, status=404, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al actualizar solicitud: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500, charset='utf-8')


def marcar_solicitud_entregada(request):
    try:
        # Verificar que la solicitud sea de tipo POST
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Obtener el id_solicitud del cuerpo de la solicitud JSON
            id_solicitud = body_data.get("id_solicitud")

            # Obtener la solicitud existente por su id_solicitud
            solicitud = SolicitudRecoleccion.objects.get(id_solicitud=id_solicitud)

            # Actualizar el campo estado a 'E' (Entregada)
            solicitud.estado = 'E'

            # Actualizar la fecha_asig con la fecha y hora actuales (si no está asignada)
            solicitud.fecha_asig = solicitud.fecha_asig or datetime.now()

            # Actualizar la fecha_fin con la fecha y hora actuales
            solicitud.fecha_fin = datetime.now()

            # Guardar los cambios en la base de datos
            solicitud.save()

            return JsonResponse({"success": True, "message": f"Solicitud {id_solicitud} marcada como entregada"}, charset='utf-8')

        else:
            # Devolver un error si el método de solicitud no es POST
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except SolicitudRecoleccion.DoesNotExist:
        # Devolver un error si la solicitud no existe
        return JsonResponse({"error": "La solicitud no existe"}, status=404, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al marcar solicitud como entregada: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, status=500, charset='utf-8')

def agregar_calificacion(request):
    try:
        # Verificar que la solicitud sea de tipo POST
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Obtener los datos necesarios del cuerpo de la solicitud JSON
            id_reciclador = body_data.get("id_reciclador")
            id_usuario = body_data.get("id_usuario")
            calificacion_nueva = body_data.get("calificacion")
            observacion = body_data.get("observacion")

            # Verificar si el reciclador existe
            reciclador = Reciclador.objects.get(id_reciclador=id_reciclador)

            # Crear una nueva calificación
            calificacion = Calificacion.objects.create(
                id_reciclador=reciclador,
                id_usuario=Usuario.objects.get(id_usuario=id_usuario),
                calificacion=calificacion_nueva,
                observacion=observacion
            )

            # Calcular el promedio de las calificaciones para el reciclador
            calificaciones_reciclador = Calificacion.objects.filter(id_reciclador=reciclador)
            promedio_calificaciones = (
                calificaciones_reciclador.aggregate(promedio=models.Avg('calificacion'))['promedio']
                if calificaciones_reciclador.exists() else 0
            )

            # Actualizar el campo calificacion del reciclador con el promedio
            reciclador.calificacion = promedio_calificaciones
            reciclador.save()

            return JsonResponse({"success": True, "message": "Calificación agregada exitosamente"}, charset='utf-8')

        else:
            # Devolver un error si el método de solicitud no es POST
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except Reciclador.DoesNotExist:
        # Devolver un error si el reciclador no existe
        return JsonResponse({"error": "El reciclador no existe"}, status=404, charset='utf-8')

    except Usuario.DoesNotExist:
        # Devolver un error si el usuario no existe
        return JsonResponse({"error": "El usuario no existe"}, status=404, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al agregar calificación: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la calificación: {str(e)}"}, status=500, charset='utf-8')
    

def crear_reporte(request):
    try:
        # Verificar que la solicitud sea de tipo POST
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Obtener los datos necesarios del cuerpo de la solicitud JSON
            id_usuario = body_data.get("id_usuario")
            id_usuario_rep = body_data.get("id_usuario_rep")
            descripcion = body_data.get("descripcion")

            # Verificar si los usuarios existen
            usuario = Usuario.objects.get(id_usuario=id_usuario)
            usuario_rep = Usuario.objects.get(id_usuario=id_usuario_rep)

            # Crear un nuevo reporte
            reporte = ReporteDenuncias.objects.create(
                id_usuario=usuario,
                id_usuario_rep=usuario_rep,
                descripcion=descripcion,
                estado='A'  # 'A' representa "Activo" como valor predeterminado
            )

            return JsonResponse({"success": True, "message": "Reporte creado exitosamente"}, charset='utf-8')

        else:
            # Devolver un error si el método de solicitud no es POST
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except Usuario.DoesNotExist:
        # Devolver un error si uno de los usuarios no existe
        return JsonResponse({"error": "Uno de los usuarios no existe"}, status=404, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al crear el reporte: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar el reporte: {str(e)}"}, status=500, charset='utf-8')


def marcar_reporte_inactivo(request):
    try:
        # Verificar que la solicitud sea de tipo POST
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Obtener el id_reporte del cuerpo de la solicitud JSON
            id_reporte = body_data.get("id_reporte")

            # Obtener el reporte existente por su id_reporte
            reporte = ReporteDenuncias.objects.get(id_reporte=id_reporte)

            # Actualizar el campo estado a 'I' (Inactivo)
            reporte.estado = 'I'

            # Guardar los cambios en la base de datos
            reporte.save()

            return JsonResponse({"success": True, "message": f"Reporte {id_reporte} marcado como inactivo"}, charset='utf-8')

        else:
            # Devolver un error si el método de solicitud no es POST
            return JsonResponse({"error": "Método no permitido"}, status=405, charset='utf-8')

    except ReporteDenuncias.DoesNotExist:
        # Devolver un error si el reporte no existe
        return JsonResponse({"error": "El reporte no existe"}, status=404, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al marcar el reporte como inactivo: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar el reporte: {str(e)}"}, status=500, charset='utf-8')


''' 
    
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

'''