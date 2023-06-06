from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# ------------------------------ AUTENTICACIÓN

# Create your views here.

# clase creadora de formulario de registro de usuario
class VRegistro(View):
    # genera el formulario en la vista de autenticación
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})
    
    # redirige al usuario a inicio y envía la información del formulario
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("Home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form":form})

        

