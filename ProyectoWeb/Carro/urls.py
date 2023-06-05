from django.urls import path
from . import views

# ------------------------------ CARRO

# name space, permite agregar carro antes del nombre de la ruta
# evita colisiones de rutas en caso de tener mismo nombre
app_name = "carro"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]
