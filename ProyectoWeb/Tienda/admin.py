from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonli_fields = ("created", "updated")
    

class ProductoAdmin(admin.ModelAdmin):
    readonli_fields = ("created", "updated")
    

# registro de modelos en Panel Administrativo
admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)


