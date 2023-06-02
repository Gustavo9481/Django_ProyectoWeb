from django.db import models

# Create your models here. - SERVICIOS

# Clase para la creacion de servicios
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='Servicios')   # subcarpeta
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"
        
    def __str__(self):
        return self.titulo
        

# Hacer migraciones despues de cada actualizacion o cambio
