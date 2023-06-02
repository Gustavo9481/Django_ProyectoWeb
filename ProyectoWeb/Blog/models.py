from django.db import models
from django.contrib.auth.models import User   # usuarios para postear

# Create your models here. - BLOG

# Clase para la creacion de categorias de los post
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        
    def __str__(self):
        return self.nombre
        

# Clase para la creacion de post
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='Blog', null=True, blank=True)   # subcarpeta - imagen opcional
    autor = models.ForeignKey(User, on_delete=models.CASCADE)   # usuario y eliminacion en cascada
    categorias = models.ManyToManyField(Categoria)   # permite uso de varias categorias 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"
        
    def __str__(self):
        return self.titulo