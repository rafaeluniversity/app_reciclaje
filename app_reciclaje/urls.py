"""
URL configuration for app_reciclaje project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

from api.views import (registroEmpresa, registroPersona,
                       registroReciclador, login_view,
                       generar_solicitud, actualizar_solicitud,
                       marcar_solicitud_entregada, agregar_calificacion,
                       crear_reporte, marcar_reporte_inactivo, crearRol,
                       obtenerInformacionUsuario, listaRecicladoresEmpresa,
                       actualizacionDeCampos, obtener_territorios, guardar_imagen,
                       actualizar_estado_reciclador, enviar_solicitud, tipos_materiales_activos,
                       ingresar_registro_reciclaje, crear_tipo_material, actualizar_registro_reciclaje,
                       obtener_registro_reciclaje)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('docs/', include_docs_urls(title='Api Documentation')),
    path('api/v1/registro_empresa/', registroEmpresa, name='registro_empresa'),
    path('api/v1/registro_persona/', registroPersona, name='registro_persona'),
    path('api/v1/registro_reciclador/', registroReciclador, name='registro_reciclador'),
    path('api/v1/login_view/', login_view, name='login_view'),
    path('api/v1/generar_solicitud/', generar_solicitud, name='generar_solicitud'),
    path('api/v1/actualizar_solicitud/', actualizar_solicitud, name='actualizar_solicitud'),
    path('api/v1/marcar_solicitud_entregada/', marcar_solicitud_entregada, name='marcar_solicitud_entregada'),
    path('api/v1/agregar_calificacion/', agregar_calificacion, name='agregar_calificacion'),
    path('api/v1/crear_reporte/', crear_reporte, name='crear_reporte'),
    path('api/v1/marcar_reporte_inactivo/', marcar_reporte_inactivo, name='marcar_reporte_inactivo'),
    path('api/v1/crearRol/', crearRol, name='crear_rol'),
    path('api/v1/obtener_informacion_usuario/', obtenerInformacionUsuario, name='obtener_informacion_usuario'),
    path('api/v1/lista_recicladores_empresa/', listaRecicladoresEmpresa, name='lista_recicladores_empresa'),
    path('api/v1/actualizar_usuario/', actualizacionDeCampos, name='actualizar_usuario'),
    path('api/v1/territorios/', obtener_territorios, name='obtener_territorios'),
    path('api/v1/guardar_imagen/', guardar_imagen, name='guardar_imagen'),  # Añade la nueva URL para la carga de imágenes
    path('api/v1/actualizar_estado_reciclador/', actualizar_estado_reciclador, name='actualizar_estado_reciclador'),
    path('api/v1/enviar_solicitud_reciclador/', enviar_solicitud, name='enviar_solicitud_reciclador'),
    path('api/v1/tipos_materiales_activos/', tipos_materiales_activos, name='tipos_materiales_activos'),
    path('api/v1/ingresar_registro_reciclaje/', ingresar_registro_reciclaje, name='ingresar_registro_reciclaje'),
    path('api/v1/crear_tipo_material/', crear_tipo_material, name='crear_tipo_material'),
    path('api/v1/actualizar_registro_reciclaje/', actualizar_registro_reciclaje, name='actualizar_registro_reciclaje'),
    path('api/v1/obtener_registro_reciclaje/', obtener_registro_reciclaje, name='obtener_registro_reciclaje'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)