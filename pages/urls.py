from django.urls import path
from .views import index, crear_oferta, crear_cv

urlpatterns = [
    path('', index, name="oferta"),
    path('oferta/crear', crear_oferta, name="crear_oferta"),
    path('oferta/crear_cv', crear_cv, name="crear_cv"),
]