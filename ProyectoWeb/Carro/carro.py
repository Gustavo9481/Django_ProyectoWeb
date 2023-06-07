# ------------------------------ CARRO
# Aplicación para carro de compras
# Clase creadora de carro de compras

class Carro:
    # constructor del carro de compras
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        # de no existir de crea el carro / else: vuelve a la sesión del usuario
        if not carro:
            carro = self.session["carro"] = {}

        self.carro = carro

    # método para agregar productos al carro
    def agregar(self, producto):
        # si el producto -NO- está en el carro
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            # si el producto -SI- está en el carro
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break
        # guardado de la sesión para ambos casos (actualización del carro)
        self.guardar_carro()
    
    # método para guardar los cambios o actualizar el carro al agregar prodscutos
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    # eliminar productos del carro
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    # restar una unidad a un producto en el carro
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = float(value["precio"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    # limpiar el carrpo de compras en su totalidad
    def limpiar_carro(self):
        carro = self.session["carro"] = {}
        self.session.modified = True    





