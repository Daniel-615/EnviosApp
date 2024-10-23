from django.urls import path
from .views import actualizar_asignacion,crear_asignacion

urlpatterns = [
    path('asignaciones/editar/<uuid:id>/', actualizar_asignacion, name='actualizar_asignacion'),
    path('asignaciones/crear/',crear_asignacion,name='crear_asignacion')
]
