from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

# ------------------------------ CONTACTO
def contacto(request):
    formulario_contacto = FormularioContacto()   # instancia de FormularioContacto
    
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            # envio de email
            email = EmailMessage("ProyectoWeb - Formulario de contacto\nNombre:{}\nEmail:{}\nContenido:{}".format(nombre, email, contenido),
                "",["guscode.apps@gmail.com"], reply_to=[email])
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")
        
    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})