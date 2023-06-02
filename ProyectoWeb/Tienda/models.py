from django.db import models

# ------------------------------ TIENDA

# Create your models here.

# Modelo de tabla de categorias
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="CategoriaProd"
        verbose_name_plural="CategoriasProd"
        
    def __str__(self):
        return self.nombre
        

# Modelo de tabla de productos
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="Tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        
    def __str__(self):
        return self.nombre
    
    