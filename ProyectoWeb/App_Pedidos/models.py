from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import Producto
from django.db.models import F, Sum, FloatField

# ------------------------------ PEDIDOS

User = get_user_model()   # obtención del usuario autenticado

# Create your models here.

# tabla de información general del pedido
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ped = str(self.id)
        return ped  #self.id

    @property  
    def total(self):
        return lineapedido_set.aggregate(
                total = Sum(F('precio')*F('cantidad'), output_field=FloatField())
                )['total']

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']



# tabla para el detalle del pedido
class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cant = str(self.cantidad)
        return f"{cant} unidades - producto: {self.producto.nombre}"

    class Meta:
        db_table = 'lineapedido'
        verbose_name = 'linea pedido'
        verbose_name_plural = 'lineas pedidos'
        ordering = ['id']




