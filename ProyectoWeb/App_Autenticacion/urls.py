from django.urls import path
from .views import VRegistro, cerrar_sesion, loguear

# ------------------------------ AUTENTICACIÓ# 

urlpatterns = [
    path('', VRegistro.as_view(),name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
    path('login', loguear, name="Login"),
]


