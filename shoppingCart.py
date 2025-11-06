class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad=1):
        if cantidad < 0:
            return "Error: No se puede agregar una cantidad negativa de productos al carrito."
        for _ in range(cantidad):
            self.productos.append(producto)

    def eliminar_producto(self, producto):
        if not self.productos:
            return "El carrito está vacío. No se puede eliminar ningún producto."

        if producto not in self.productos:
            return f"El producto {producto.nombre} no está en el carrito."

        for i, prod in enumerate(self.productos):
            if prod.nombre == producto.nombre:
                del self.productos[i]
                return f"Producto {producto.nombre} eliminado del carrito."

    def calcular_subtotal(self):
        return sum(producto.precio for producto in self.productos)

    def calcular_total_con_descuento(self, descuento=0.0):
        subtotal = self.calcular_subtotal()
        total_con_descuento = subtotal * (1 - descuento)
        return total_con_descuento * 1.16

    def estado_carrito(self):
        return len(self.productos) > 0
