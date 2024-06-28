from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'roles', views.RolesViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'usuarios-persona', views.UsuarioPersonaViewSet)
router.register(r'usuarios-empresa', views.UsuarioEmpresaViewSet)
router.register(r'relaciones-empresa', views.RelacionEmpresaViewSet)
router.register(r'recicladores', views.RecicladorViewSet)
router.register(r'calificaciones', views.CalificacionViewSet)
router.register(r'archivos', views.ArchivoViewSet)
router.register(r'carnet-recolectores', views.CarnetRecolectoresViewSet)
router.register(r'solicitudes-recoleccion', views.SolicitudRecoleccionViewSet)
router.register(r'archivos-solicitudes', views.ArchivosSolicitudesViewSet)
router.register(r'reportes-denuncias', views.ReporteDenunciasViewSet)
router.register(r'archivos-reportes', views.ArchivosReportesViewSet)
router.register(r'imagenes', views.ImagenViewSet)


urlpatterns = [
    path('', include(router.urls))
]
