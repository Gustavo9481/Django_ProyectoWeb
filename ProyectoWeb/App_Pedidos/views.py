from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from Carro.carro import Carro
from App_Pedidos.models import Pedido, LineaPedido

# ------------------------------ PEDIDOS

# Create your views here.

@login_required(login_url=("/autenticacion/logear"))
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value['cantidad'],
            user = request.user,
            pedido = pedido
            ))

    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
            pedido = pedido,
            lineas_pedido = lineas_pedido,
            nombreusuario= request.user.username,
            emailusuario = request.user.email
            )

    messages.success(request, "Su pedido ha sido procesado exitosamente")
    
    return redirect("../tienda")


def enviar_mail(**kwargs):
    asunto = "Gracias por realizar su pedido"
    mensaje = render_to_string(emails/pedido.html, {
            "pedido": kwargs.get("pedido"),
            "lineas_pedido": kwargs.get("lineas_pedido"),
            "nombreusuario": kwargs.get("nombreusuario")
        })
    mensaje_texto = strip_tags(mensaje)
    from_email = "gestion_pedidos@gmail.com"
    to = kwargs.get("emailusuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
