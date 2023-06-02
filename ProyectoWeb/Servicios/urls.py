from django.urls import path
from . import views
 
# ------------------------------ SERVICIOS

# vista general de servicios
urlpatterns = [
    path('', views.servicios, name="Servicios"),
]

