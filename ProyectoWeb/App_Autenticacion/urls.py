from django.urls import path
from .views import VRegistro

# ------------------------------ AUTENTICACIÓ# 

urlpatterns = [
    path('', VRegistro.as_view(),name="Autenticacion"),
]


