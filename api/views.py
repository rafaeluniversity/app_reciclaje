from rest_framework import viewsets
from django.db import models
from django.http import JsonResponse
#from django.db import transaction, connection
import json
from django.contrib.auth.hashers import check_password, make_password
from datetime import datetime
from django.db.models import Value, CharField
from django.db.models.functions import Concat
from django.db.models.functions import Replace
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

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
    ArchivosReportesSerializer,
    ImagenSerializer
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
    ArchivosReportes,
    Territorio,
    Imagen,
    TipoMaterial,
    RegistroReciclaje
)

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

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
"""
def guardar_imagen(request):
    try:
        if request.method == "POST":
            # Decodificar y cargar los datos del cuerpo de la solicitud JSON
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Extraer datos del cuerpo de la solicitud
            imagen_data = body_data.get("imagen")

            # Crear un nuevo objeto de Imagen
            imagen = Imagen(imagen=imagen_data)

            # Guardar el objeto en la base de datos
            imagen.save()

            # Retornar el ID y la URL de la imagen creada
            return JsonResponse({"id_imagen": imagen.id_imagen, "url_imagen": imagen.get_image_url()}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al guardar la imagen: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')
"""

def enviar_solicitud(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        id_reciclador = body_data.get("id_reciclador")
        id_empresa = body_data.get("id_empresa")

        try:
            reciclador = Reciclador.objects.get(id_reciclador=id_reciclador)
            try:
                empresa = UsuarioEmpresa.objects.get(id_empresa=id_empresa)
                reciclador.estado_reciclador = "E"  # Cambiar estado a "Espera"
                reciclador.id_empresa = id_empresa  # Asignar el id de la empresa
                reciclador.save()
                return JsonResponse({"message": "Solicitud enviada correctamente", "success": True})
            except UsuarioEmpresa.DoesNotExist:
                return JsonResponse({"error": "La empresa especificada no existe"})
        except Reciclador.DoesNotExist:
            return JsonResponse({"error": "Reciclador no encontrado"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Método no permitido"})

def guardar_imagen(request):
    try:
        if request.method == "POST":
            # Verificar si la solicitud contiene datos de archivo
            if 'imagen' in request.FILES:
                # Extraer el archivo de la solicitud
                imagen = request.FILES['imagen']

                # Crear un nuevo objeto de Imagen
                nueva_imagen = Imagen(imagen=imagen)

                # Guardar la imagen en la base de datos
                nueva_imagen.save()

                # Retornar el ID y la URL de la imagen creada
                return JsonResponse({"data": {"id_imagen": nueva_imagen.id_imagen, "url_imagen": nueva_imagen.get_image_url()}, "success": True}, charset='utf-8', safe=False)
            else:
                return JsonResponse({"error": "No se proporcionó ninguna imagen en la solicitud"}, charset='utf-8')
        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al guardar la imagen: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')

def crearRol(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Extraer datos del cuerpo de la solicitud
            descripcion = body_data.get("descripcion")

            # Verificar si la descripción del rol ya existe
            if Roles.objects.filter(descripcion=descripcion).exists():
                return JsonResponse({"error": "La descripción del rol ya existe"}, charset='utf-8')

            # Crear un nuevo objeto de Rol
            rol = Roles(
                descripcion=descripcion
            )

            # Guardar el objeto en la base de datos
            rol.save()

            return JsonResponse({"success": True, "message": "Rol creado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al crear el rol: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')

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
            url_foto = body_data.get("url_foto")
            telefono = body_data.get("telefono")
            ruc = body_data.get("ruc")  # Agregar el campo ruc

            # Verificar la unicidad del correo electrónico, razón social y RUC
            if UsuarioEmpresa.objects.filter(correo=correo).exists():
                return JsonResponse({"error": "El correo electrónico ya está en uso"}, charset='utf-8')

            if UsuarioEmpresa.objects.filter(razon_social=razon_social).exists():
                return JsonResponse({"error": "La razón social ya está en uso"}, charset='utf-8')

            if UsuarioEmpresa.objects.filter(ruc=ruc).exists():
                return JsonResponse({"error": "El RUC ya está en uso"}, charset='utf-8')

            # Convertir la cadena JSON de redes en un diccionario si es necesario
            if isinstance(redes, str):
                redes = json.loads(redes)

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
                id_rol=Roles.objects.get(id_rol='rol_002'),  # Asignar el rol correspondiente,
                url_foto=url_foto,
                telefono=telefono,
                ruc=ruc  # Agregar el campo ruc
            )

            # Guardar el objeto en la base de datos
            usuario_empresa.save()

            return JsonResponse({"success": True, "message": "UsuarioEmpresa registrado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error en registroEmpresa: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')

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
            fec_nac = datetime.strptime(body_data.get("fec_nac"), '%Y-%m-%d').date()
            genero = body_data.get("genero")
            url_foto = body_data.get("url_foto")
            cedula = body_data.get("cedula")
            telefono = body_data.get("telefono")

            # Verificar la unicidad del correo electrónico
            if Usuario.objects.filter(correo=correo).exists():
                return JsonResponse({"error": "El correo electrónico ya está en uso"}, charset='utf-8')

            # Crear un nuevo objeto UsuarioPersona
            usuario_persona = UsuarioPersona(
                correo=correo,
                clave=make_password(clave),
                nombres=nombres,
                apellidos=apellidos,
                provincia=provincia,
                ciudad=ciudad,
                direccion=direccion,
                fec_nac=fec_nac,
                genero=genero,
                id_rol=Roles.objects.get(id_rol='rol_004'),  # Asignar el rol correspondiente
                url_foto=url_foto,
                cedula=cedula,
                telefono=telefono
            )

            # Guardar el objeto en la base de datos
            usuario_persona.save()

            return JsonResponse({"success": True, "message": "UsuarioPersona registrado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error en registroPersona: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')

#
def registroReciclador(request):
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
            fec_nac = datetime.strptime(body_data.get("fec_nac"), '%Y-%m-%d').date()
            genero = body_data.get("genero")
            id_empresa = body_data.get("id_empresa")
            calificacion_reciclador = body_data.get("calificacion_reciclador")
            nacionalidad = body_data.get("nacionalidad")
            url_foto = body_data.get("url_foto")
            cedula = body_data.get("cedula")
            telefono = body_data.get("telefono")

            # Verificar si el campo id_empresa está presente y no está vacío
            if not id_empresa:
                return JsonResponse({"error": "El campo 'id_empresa' es obligatorio"}, charset='utf-8')

            # Verificar si el id_empresa existe en la tabla UsuarioEmpresa
            if not UsuarioEmpresa.objects.filter(id_empresa=id_empresa).exists():
                return JsonResponse({"error": "El 'id_empresa' proporcionado no existe"}, charset='utf-8')

            # Verificar la unicidad del correo electrónico
            if Usuario.objects.filter(correo=correo).exists():
                return JsonResponse({"error": "El correo electrónico ya está en uso"}, charset='utf-8')

            # Crear un nuevo objeto Reciclador, que hereda de UsuarioPersona
            reciclador = Reciclador(
                correo=correo,
                clave=make_password(clave),
                nombres=nombres,
                apellidos=apellidos,
                provincia=provincia,
                ciudad=ciudad,
                direccion=direccion,
                fec_nac=fec_nac,
                genero=genero,
                id_rol=Roles.objects.get(id_rol='rol_003'),  # Asignar el rol correspondiente
                calificacion_reciclador=calificacion_reciclador,
                nacionalidad=nacionalidad,
                id_empresa=id_empresa,
                url_foto=url_foto,
                cedula=cedula,
                telefono=telefono
            )

            # Guardar el objeto Reciclador en la base de datos
            reciclador.save()

            return JsonResponse({"success": True, "message": "Reciclador registrado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error en registroReciclador: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')

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
                if hasattr(user, 'usuariopersona'):
                    # Usuario es una persona
                    nombre_corto = f"{user.usuariopersona.nombres.split()[0]} {user.usuariopersona.apellidos.split()[0]}"
                elif hasattr(user, 'usuarioempresa'):
                    # Usuario es una empresa
                    nombre_corto = f"{user.usuarioempresa.razon_social}"
                else:
                    # Otro tipo de usuario sin nombre corto definido
                    nombre_corto = ""

                user_data = {
                    "id_usuario": user.id_usuario,
                    "rol": user.id_rol.descripcion,
                    "nombre_corto": nombre_corto,
                    "url_foto": user.url_foto
                }

                return JsonResponse({"success": True, "data": user_data})
            else:
                # Las credenciales no coinciden o el usuario no existe
                return JsonResponse({"error": "Credenciales incorrectas"})
        else:
            return JsonResponse({"error": "Método no permitido"})

    except Exception as e:
        # Utiliza el sistema de registro de Django para manejar errores
        # logging.error(f"Error en la vista de login: {str(e)}")
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"})

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
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Usuario.DoesNotExist:
        return JsonResponse({"error": "El usuario no existe"}, charset='utf-8')

    except Reciclador.DoesNotExist:
        return JsonResponse({"error": "El reciclador no existe"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al generar solicitud: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')


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
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except SolicitudRecoleccion.DoesNotExist:
        # Devolver un error si la solicitud no existe
        return JsonResponse({"error": "La solicitud no existe"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al actualizar solicitud: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')


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
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except SolicitudRecoleccion.DoesNotExist:
        # Devolver un error si la solicitud no existe
        return JsonResponse({"error": "La solicitud no existe"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al marcar solicitud como entregada: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')

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

            calificacion.save()

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
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Reciclador.DoesNotExist:
        # Devolver un error si el reciclador no existe
        return JsonResponse({"error": "El reciclador no existe"}, charset='utf-8')

    except Usuario.DoesNotExist:
        # Devolver un error si el usuario no existe
        return JsonResponse({"error": "El usuario no existe"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al agregar calificación: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la calificación: {str(e)}"}, charset='utf-8')


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

            reporte.save()

            return JsonResponse({"success": True, "message": "Reporte creado exitosamente"}, charset='utf-8')

        else:
            # Devolver un error si el método de solicitud no es POST
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Usuario.DoesNotExist:
        # Devolver un error si uno de los usuarios no existe
        return JsonResponse({"error": "Uno de los usuarios no existe"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al crear el reporte: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar el reporte: {str(e)}"}, charset='utf-8')


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
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except ReporteDenuncias.DoesNotExist:
        # Devolver un error si el reporte no existe
        return JsonResponse({"error": "El reporte no existe"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al marcar el reporte como inactivo: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar el reporte: {str(e)}"}, charset='utf-8')

def obtenerInformacionUsuario(request):
    try:

        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Obtener el id del usuario
            usuario_ptr_id = body_data.get("id_usuario")

            # Verificar si el usuario existe
            usuario_persona = UsuarioPersona.objects.get(usuario_ptr_id=usuario_ptr_id)
            usuario_rol = usuario_persona.id_rol.id_rol

            reciclador = usuario_persona.reciclador

            print("ID del usuario recibido:", usuario_ptr_id)
            print("Usuario Rol:", usuario_rol)
            print("Reciclador:", reciclador)

            # Obtener información personal del usuario persona
            informacion_personal = {
                "cedula": {
                    "label": "Cédula",
                    "value": usuario_persona.cedula,
                    "type": "text",
                    "editable": False,
                    "validation": "cedula",
                    "maxLength": 10
                },
                "nombres": {
                    "label": "Nombres",
                    "value": usuario_persona.nombres,
                    "type": "text",
                    "editable": False,
                    "validation": "text",
                    "maxLength": 50
                },
                "apellidos": {
                    "label": "Apellidos",
                    "value": usuario_persona.apellidos,
                    "type": "text",
                    "editable": False,
                    "validation": "text",
                    "maxLength": 50
                },
                "telefono": {
                    "label": "Teléfono",
                    "value": usuario_persona.telefono,
                    "type": "text",
                    "editable": True,
                    "validation": "number10",
                    "maxLength": 10
                },
                "correo": {
                    "label": "Correo",
                    "value": usuario_persona.correo,
                    "type": "email",
                    "editable": True,
                    "validation": "email",
                    "maxLength": 100
                },
                "sexo": {
                    "label": "Sexo",
                    "value": usuario_persona.genero,
                    "type": "select",
                    "editable": True,
                    "validation": "select"
                },
                "fecha_nacimiento": {
                    "label": "Fecha de nacimiento",
                    "value": usuario_persona.fec_nac.strftime('%Y-%m-%d'),
                    "type": "date",
                    "editable": True,
                    "validation": "date18"
                },
                "direccion": {
                    "label": "Dirección",
                    "value": usuario_persona.direccion,
                    "type": "textarea",
                    "editable": True,
                    "validation": "textarea",
                    "maxLength": 500
                },

            }

            # Verificar si el usuario es un reciclador
            if usuario_rol == 'rol_003':
                # Obtener información del reciclador si existe
                reciclador = usuario_persona.reciclador

                # Obtener información de la empresa directamente de UsuarioEmpresa
                empresa_reciclador = UsuarioEmpresa.objects.filter(id_empresa=reciclador.id_empresa).first()

                if empresa_reciclador:

                    reciclador_info = {
                    "calificacion": reciclador.calificacion_reciclador,
                    "organizacion": {
                        "razon_social": empresa_reciclador.razon_social,
                        "link_perfil": "profile/organizacionx",
                        "direccion": empresa_reciclador.direccion,
                        "contact": {
                            "telefono": empresa_reciclador.telefono,
                            "correo": empresa_reciclador.correo,
                            "facebook": empresa_reciclador.redes.get("facebook"),
                            "instagram": empresa_reciclador.redes.get("instagram"),
                            "twitter": empresa_reciclador.redes.get("twitter")
                        }
                    }
                }
                else:
                    reciclador_info = {
                    "calificacion": reciclador.calificacion_reciclador,
                    "organizacion": {
                        "razon_social": "",
                        "link_perfil": "",
                        "direccion": "",
                        "contact": {
                            "telefono": "",
                            "correo": "",
                            "facebook": "",
                            "instagram": "",
                            "twitter": ""
                        }
                    }
                }



                # Combinar información personal del usuario persona y del reciclador si existe
                response_data = {
                    "informacion_personal": informacion_personal,
                    "url_foto": usuario_persona.url_foto,
                    **reciclador_info
                }
            else:
                # Si el usuario no es un reciclador, solo devuelve la información personal
                response_data = {
                    "informacion_personal": informacion_personal,
                    "url_foto": usuario_persona.url_foto
                }
            print("todo correcto, data:", response_data)

            return JsonResponse({"data": response_data, "success": True}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except UsuarioPersona.DoesNotExist:
        return JsonResponse({"error": "El usuario no existe"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error en obtenerInformacionUsuario: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')

def listaRecicladoresEmpresa(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Obtener el id_empresa del cuerpo de la solicitud JSON
            id_empresa = body_data.get("id_empresa")
            estado_reciclador = body_data.get("estado_reciclador")

            # Verificar si el id_empresa es válido
            if not id_empresa:
                return JsonResponse({"error": "Se requiere el parámetro id_empresa"})

            # Filtrar los recicladores por id_empresa y estado_reciclador
            recicladores = Reciclador.objects.filter(id_empresa=id_empresa, estado_reciclador=estado_reciclador)

            # Serializar los recicladores para devolverlos en la respuesta
            recicladores_data = []
            for reciclador in recicladores:
                fec_nac_str = reciclador.fec_nac.strftime('%Y-%m-%d')
                fec_nac = datetime.strptime(fec_nac_str, '%Y-%m-%d')
                fecha_actual = datetime.now();

                # Llama a la segunda vista con un HttpRequest válido
                usuario_request = HttpRequest()
                usuario_request.method = "POST"  # Establece el método como POST
                usuario_request._body = json.dumps({"id_usuario": reciclador.id_usuario}).encode('utf-8')  # Crea el cuerpo de la solicitud
                respuesta_segunda_vista = obtenerInformacionUsuario(usuario_request)
                data = json.loads(respuesta_segunda_vista.content.decode('utf-8'))

                if data.get("success"):
                    reciclador_info = {
                        "id_usuario": reciclador.id_usuario,
                        "id_reciclador": reciclador.id_reciclador,
                        "nombres": reciclador.nombres,
                        "apellidos": reciclador.apellidos,
                        "nombre_corto": f"{reciclador.nombres.split()[0]} {reciclador.apellidos.split()[0]}",
                        "correo": reciclador.correo,
                        "estado_reciclador": reciclador.estado_reciclador,
                        "provincia": reciclador.provincia,
                        "ciudad": reciclador.ciudad,
                        "direccion_corta": f"{reciclador.provincia.lower().capitalize()}, {reciclador.ciudad.lower().capitalize()}",
                        "direccion": reciclador.direccion,
                        "fec_nac": fec_nac_str,
                        "edad": fecha_actual.year - fec_nac.year - ((fecha_actual.month, fecha_actual.day) < (fec_nac.month, fec_nac.day)),
                        "genero": reciclador.genero,
                        "cedula": reciclador.cedula,
                        "calificacion_reciclador": reciclador.calificacion_reciclador,
                        "nacionalidad": reciclador.nacionalidad,
                        "telefono": reciclador.telefono,
                        "url_foto": reciclador.url_foto,
                        "perfil": data.get("data")
                        # Agrega más campos según sea necesario
                    }
                    recicladores_data.append(reciclador_info)

            return JsonResponse({"data": recicladores_data, "success": True})

        else:
            return JsonResponse({"error": "Método no permitido"})

    except Exception as e:
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"})


def actualizar_datos_persona(persona, body_data):
    # Para el campo cedula
    persona.cedula = body_data.get("cedula", persona.cedula) if body_data.get("cedula", "") != "" else persona.cedula

    # Para los campos nombres, apellidos, provincia, ciudad, direccion, fec_nac y genero
    persona.nombres = body_data.get("nombres", persona.nombres) if body_data.get("nombres", "") != "" else persona.nombres
    persona.apellidos = body_data.get("apellidos", persona.apellidos) if body_data.get("apellidos", "") != "" else persona.apellidos
    persona.provincia = body_data.get("provincia", persona.provincia) if body_data.get("provincia", "") != "" else persona.provincia
    persona.ciudad = body_data.get("ciudad", persona.ciudad) if body_data.get("ciudad", "") != "" else persona.ciudad
    persona.direccion = body_data.get("direccion", persona.direccion) if body_data.get("direccion", "") != "" else persona.direccion
    persona.fec_nac = body_data.get("fec_nac", persona.fec_nac) if body_data.get("fec_nac", "") != "" else persona.fec_nac
    persona.genero = body_data.get("genero", persona.genero) if body_data.get("genero", "") != "" else persona.genero
    persona.telefono = body_data.get("telefono", persona.telefono) if body_data.get("telefono", "") != "" else persona.telefono
    persona.url_foto = body_data.get("url_foto", persona.url_foto) if body_data.get("url_foto", "") != "" else persona.url_foto


    # Guardar los cambios en la base de datos
    persona.save()

def actualizar_datos_empresa(empresa, body_data):
    # Para los campos razon_social, actividad_comercial, ced_rep_legal, nom_rep_legal y direccion
    empresa.razon_social = body_data.get("razon_social", empresa.razon_social) if body_data.get("razon_social", "") != "" else empresa.razon_social
    empresa.actividad_comercial = body_data.get("actividad_comercial", empresa.actividad_comercial) if body_data.get("actividad_comercial", "") != "" else empresa.actividad_comercial
    empresa.ced_rep_legal = body_data.get("ced_rep_legal", empresa.ced_rep_legal) if body_data.get("ced_rep_legal", "") != "" else empresa.ced_rep_legal
    empresa.nom_rep_legal = body_data.get("nom_rep_legal", empresa.nom_rep_legal) if body_data.get("nom_rep_legal", "") != "" else empresa.nom_rep_legal
    empresa.direccion = body_data.get("direccion", empresa.direccion) if body_data.get("direccion", "") != "" else empresa.direccion
    empresa.telefono = body_data.get("telefono", empresa.telefono) if body_data.get("telefono", "") != "" else empresa.telefono
    empresa.url_foto = body_data.get("url_foto", empresa.url_foto) if body_data.get("url_foto", "") != "" else empresa.url_foto

    # Guardar los cambios en la base de datos
    empresa.save()

def actualizar_datos_reciclador(reciclador, body_data):
    # Para los campos nombres, apellidos, provincia, ciudad, direccion, fec_nac, genero y telefono
    reciclador.nombres = body_data.get("nombres", reciclador.nombres) if body_data.get("nombres", "") != "" else reciclador.nombres
    reciclador.apellidos = body_data.get("apellidos", reciclador.apellidos) if body_data.get("apellidos", "") != "" else reciclador.apellidos
    reciclador.provincia = body_data.get("provincia", reciclador.provincia) if body_data.get("provincia", "") != "" else reciclador.provincia
    reciclador.ciudad = body_data.get("ciudad", reciclador.ciudad) if body_data.get("ciudad", "") != "" else reciclador.ciudad
    reciclador.direccion = body_data.get("direccion", reciclador.direccion) if body_data.get("direccion", "") != "" else reciclador.direccion
    reciclador.fec_nac = body_data.get("fec_nac", reciclador.fec_nac) if body_data.get("fec_nac", "") != "" else reciclador.fec_nac
    reciclador.genero = body_data.get("genero", reciclador.genero) if body_data.get("genero", "") != "" else reciclador.genero
    reciclador.telefono = body_data.get("telefono", reciclador.telefono) if body_data.get("telefono", "") != "" else reciclador.telefono
    reciclador.url_foto = body_data.get("url_foto", reciclador.url_foto) if body_data.get("url_foto", "") != "" else reciclador.url_foto

    # Guardar los cambios en la base de datos
    reciclador.save()


def actualizacionDeCampos(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        id_usuario = body_data.get("id_usuario")
        id_rol = body_data.get("id_rol")

        try:
            if id_rol == "rol_002":
                empresa = UsuarioEmpresa.objects.get(id_usuario=id_usuario)
                actualizar_datos_empresa(empresa, body_data)
            elif id_rol == "rol_003":
                reciclador = Reciclador.objects.get(id_usuario=id_usuario)
                actualizar_datos_reciclador(reciclador, body_data)
            elif id_rol == "rol_004":
                persona = UsuarioPersona.objects.get(id_usuario=id_usuario)
                actualizar_datos_persona(persona, body_data)
            else:
                # Manejar caso de rol desconocido
                return JsonResponse({"error": "Rol de usuario desconocido"})

            return JsonResponse({"message": "Datos actualizados correctamente", "success": True}, safe=False)
        except Exception as e:
            # Manejar la excepción
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Método no permitido"})


def obtener_territorios(request):
    try:
        territorios = Territorio.objects.values('id_territorio', 'id_nivel_territorial', 'id_territorio_padre', 'descripcion', 'codigo')

        territorios_json = list(territorios)

        return JsonResponse({"data": territorios_json, "success": True}, safe=False)

    except Exception as e:
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')


def actualizar_estado_reciclador(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        id_reciclador = body_data.get("id_reciclador")
        nuevo_estado = body_data.get("nuevo_estado")

        try:
            reciclador = Reciclador.objects.get(id_reciclador=id_reciclador)
            if nuevo_estado == "I":
                reciclador.estado_reciclador = nuevo_estado
                reciclador.id_empresa = None  # Eliminar id_empresa cuando el estado es inactivo
            else:
                reciclador.estado_reciclador = nuevo_estado
            reciclador.save()

            return JsonResponse({"message": "Estado de reciclador actualizado correctamente", "success": True})
        except Reciclador.DoesNotExist:
            return JsonResponse({"error": "Reciclador no encontrado"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Método no permitido"})

def crear_tipo_material(request):
    try:
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # Extraer datos del cuerpo de la solicitud
            descripcion = body_data.get("descripcion")

            # Verificar si la descripción del tipo de material ya existe
            if TipoMaterial.objects.filter(descripcion=descripcion).exists():
                return JsonResponse({"error": "La descripción del tipo de material ya existe"}, charset='utf-8')

            # Crear un nuevo objeto de TipoMaterial
            tipo_material = TipoMaterial(descripcion=descripcion)

            # Guardar el tipo de material en la base de datos
            tipo_material.save()

            return JsonResponse({"success": True, "message": "Tipo de material creado exitosamente"}, charset='utf-8')

        else:
            return JsonResponse({"error": "Método no permitido"}, charset='utf-8')

    except Exception as e:
        # Imprimir detalles de la excepción
        print(f"Error al crear el tipo de material: {str(e)}")

        # Devolver un error más informativo
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"}, charset='utf-8')


def tipos_materiales_activos(request):
    try:
        if request.method == "GET":
            # Obtener tipos de materiales activos
            tipos_activos = TipoMaterial.objects.filter(estado='A').values('descripcion', 'id_tipo_material')

            # Crear la lista de diccionarios con formato label:value
            tipos_list = [{'label': tipo['descripcion'], 'value': tipo['id_tipo_material']} for tipo in tipos_activos]

            # Retornar la lista de tipos de materiales activos
            return JsonResponse({"data":tipos_list, "success": True}, safe=False)


        else:
            # Método no permitido
            return JsonResponse({"error": "Método no permitido"})
    except Exception as e:
        # Manejar errores
        return JsonResponse({"error": f"Ocurrió un error al procesar la solicitud: {str(e)}"})

def ingresar_registro_reciclaje(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        id_material = body_data.get("id_material")
        peso = body_data.get("peso")
        id_usuario_registro = body_data.get("id_usuario_registro")
        id_reciclador = body_data.get("id_reciclador")

        try:
            material = TipoMaterial.objects.get(id_tipo_material=id_material)
            reciclador = Reciclador.objects.get(id_reciclador=id_reciclador)
            usuario_registro = Usuario.objects.get(id_usuario=id_usuario_registro)

            registro_reciclaje = RegistroReciclaje(
                id_material=material,
                peso=peso,
                id_usuario_ingreso=usuario_registro,
                id_reciclador=reciclador,
                id_usuario_modificacion=usuario_registro
            )

            registro_reciclaje.save()

            return JsonResponse({"success": True, "message": "Registro de reciclaje ingresado correctamente"})
        except TipoMaterial.DoesNotExist:
            return JsonResponse({"error": "El tipo de material especificado no existe"})
        except Reciclador.DoesNotExist:
            return JsonResponse({"error": "El reciclador especificado no existe"})
        except Usuario.DoesNotExist:
            return JsonResponse({"error": "El usuario especificado no existe"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Método no permitido"})


def actualizar_registro_reciclaje(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        id_registro = body_data.get("id_registro")
        id_material = body_data.get("id_material")
        peso = body_data.get("peso")
        id_usuario_modificacion = body_data.get("id_usuario_modificacion")
        estado = body_data.get("estado")

        try:
            registro = RegistroReciclaje.objects.get(id_registro=id_registro)
            # Actualizar los campos solicitados
            print("material", id_material, registro.id_material)
            if id_material!=None:
                registro.id_material = TipoMaterial.objects.get(id_tipo_material=id_material)
            if peso!=None:
                registro.peso = peso
            registro.id_usuario_modificacion = Usuario.objects.get(id_usuario=id_usuario_modificacion)
            registro.estado = estado
            # Guardar la fecha de modificación (la fecha_ingreso permanece igual)
            registro.save(update_fields=['id_material', 'peso', 'id_usuario_modificacion', 'estado', 'fecha_modificacion'])
            return JsonResponse({"message": "Registro de reciclaje actualizado correctamente", "success": True})
        except RegistroReciclaje.DoesNotExist:
            return JsonResponse({"error": "Registro de reciclaje no encontrado"})
        except TipoMaterial.DoesNotExist:
            return JsonResponse({"error": "Tipo de material no encontrado"})
        except Usuario.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Método no permitido"})

def obtener_registro_reciclaje(request):
    if request.method == "POST":
        body_data = json.loads(request.body)

        id_reciclador = body_data.get("id_reciclador")

        try:
            reciclador = Reciclador.objects.get(id_reciclador=id_reciclador)
            registros = RegistroReciclaje.objects.filter(id_reciclador=reciclador, estado='A')

            registros_list = []
            for registro in registros:
                material = TipoMaterial.objects.get(id_tipo_material=registro.id_material_id)
                usuario_registro = Usuario.objects.get(id_usuario=registro.id_usuario_ingreso_id)

                if hasattr(usuario_registro, 'usuarioempresa'):
                    nombre_corto = f"{usuario_registro.usuarioempresa.razon_social}"
                else:
                    nombre_corto = f"{usuario_registro.usuariopersona.nombres.split()[0]} {usuario_registro.usuariopersona.apellidos.split()[0]}"

                registros_list.append({
                    "id_registro": registro.id_registro,
                    "material": material.descripcion,
                    "peso": registro.peso,
                    "usuario_registro": nombre_corto,
                    "fecha_registro": registro.fecha_ingreso.strftime('%Y-%m-%d')
                })

            return JsonResponse({"data":registros_list, "success": True}, safe=False)
        except Reciclador.DoesNotExist:
            return JsonResponse({"error": "No se encontró el reciclador"})
        except RegistroReciclaje.DoesNotExist:
            return JsonResponse({"error": "No se encontraron registros de reciclaje para este reciclador"})
        except TipoMaterial.DoesNotExist:
            return JsonResponse({"error": "No se encontró información del material"})
        except UsuarioPersona.DoesNotExist:
            return JsonResponse({"error": "No se encontró información del usuario persona"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Método no permitido"})

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