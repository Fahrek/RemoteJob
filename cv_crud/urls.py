from django.urls import path
from .views import cv_create, cv_generate


urlpatterns = [
    path('crear', cv_create, name="crear_cv"),
    path('mostrar', cv_generate, name="leer_cv"),
    # path('eliminar/<int:id>',   cv_delete, name="borrar_cv"),
    # path('actualizar/<int:id>', cv_update, name="modificar_cv"),
    # path('update/<int:id>',     cv_update, name='actualizar_cv')
]