from django.shortcuts import render
from .carro import Carro
from Tienda.models import Producto
from django.shortcuts import redirect


# ------------------------------ BLOG

# Create your views here.

# Agregar
# crea carro / obtiene id producto / agrega producto a carro / redirije a tienda
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")


# Eliminar
# crea carro / obtiene id producto / elimina producto del carro / redirije a tienda
def eliminar_producto(request, producto_id):    
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")


# Restar 
# crea carro / obtiene id producto / resta producto a carro / redirije a tienda
def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")


# Limpiar
# crea carro / limpiar carro / redirije a tienda
def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")


