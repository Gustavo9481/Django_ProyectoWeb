from django.urls import path
from . import views

# ------------------------------ TIENDA

# vista general de tienda
urlpatterns = [
    path('', views.tienda, name="Tienda"),
]
