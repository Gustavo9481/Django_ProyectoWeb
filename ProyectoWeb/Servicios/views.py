from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.

# ------------------------------ SERVICIOS
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})