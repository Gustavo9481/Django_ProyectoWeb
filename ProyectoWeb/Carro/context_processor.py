 # ------------------------------ CARRO
   
# variable global almacenamiento de total de compra
# Función registrada en settings = TEMPLATES
def importe_total_carro(request):
    total = 0
    # if request.user.is_authenticated:   => se usará a futuro
    for key, value in request.session["carro"].items():
        total = total + float(value["precio"])
    return {"importe_total_carro": total}


# TODO: sistema de autenticación
