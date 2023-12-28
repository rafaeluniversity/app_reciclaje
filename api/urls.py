from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'roles', views.RolesViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'roles_usuarios', views.RolesUsuariosViewSet)
router.register(r'usuarios_empresas', views.UsuarioEmpresaViewSet)
router.register(r'usuarios_personas', views.UsuarioPersonaViewSet)
router.register(r'recolectores', views.RecolectorViewSet)
router.register(r'calificaciones', views.CalificacionesViewSet)
router.register(r'solicitudes_recoleccion', views.SolicitudRecoleccionViewSet)
router.register(r'archivos', views.ArchivosViewSet)
router.register(r'carnet_recolector', views.CarnetRecolectorViewSet)
router.register(r'archivos_solicitudes', views.ArchivosSolicitudesViewSet)
router.register(r'reportes_denuncias', views.ReportesDenunciasViewSet)
router.register(r'archivos_reportes', views.ArchivosReportesViewSet)
router.register(r'relacion_empresas', views.RelacionEmpresaViewSet)

urlpatterns = [
    path('', include(router.urls))
]
