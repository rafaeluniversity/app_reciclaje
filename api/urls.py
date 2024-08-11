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
router.register(r'carrusel-fotos', views.CarruselFotoViewSet, basename='carrusel-fotos')
router.register(r'quienes-somos', views.QuienesSomosViewSet, basename='quienes-somos')
router.register(r'secciones', views.SeccionViewSet, basename='secciones')
router.register(r'parrafos', views.ParrafoViewSet, basename='parrafos')
router.register(r'timelines', views.TimelineViewSet, basename='timelines')
router.register(r'pasos-timeline', views.PasosTimelineViewSet, basename='pasos-timeline')
router.register(r'centros-acopio', views.CentroAcopioViewSet, basename='centros-acopio')
router.register(r'solicitud-detalle', views.SolicitudDetalleViewSet, basename='solicitud-detalle')

urlpatterns = [
    path('', include(router.urls))
]
