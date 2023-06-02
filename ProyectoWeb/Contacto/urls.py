from django.urls import path
from . import views
from django.conf import settings   
from django.conf.urls.static import static 

# ------------------------------ CONTACTO

# vista general de contacto
urlpatterns = [
    path('', views.contacto, name="Contacto"),
]