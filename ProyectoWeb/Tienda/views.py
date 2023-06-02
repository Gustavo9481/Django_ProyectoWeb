from django.shortcuts import render
from .models import Producto
# from Servicios.models import Servicio

# Create your views here.

# ------------------------------ TIENDA
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "Tienda/tienda.html", {"productos": productos})