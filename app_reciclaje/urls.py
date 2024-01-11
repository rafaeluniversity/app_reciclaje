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

from api.views import (registroEmpresa, registroPersona, 
                       registroReciclador, login_view,
                       generar_solicitud, actualizar_solicitud,
                       marcar_solicitud_entregada, agregar_calificacion,
                       crear_reporte, marcar_reporte_inactivo)


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
]