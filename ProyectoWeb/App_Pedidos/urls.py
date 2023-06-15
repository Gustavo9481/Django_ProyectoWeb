from django.urls import path
from . import views

# ------------------------------ PEDIDOS

urlpatterns = [
    path('', views.procesar_pedido, name='procesar_pedido')
]
