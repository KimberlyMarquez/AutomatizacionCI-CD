import unittest
from shoppingCart import CarritoDeCompras, Producto

class TestCarritoDeCompras(unittest.TestCase):

    def setUp(self):
        self.carrito = CarritoDeCompras()

    def test_agregar_producto(self):
        pan = Producto("Pan", 35)
        self.carrito.agregar_producto(pan, 1)
        self.assertEqual(len(self.carrito.productos), 1)

    def test_agregar_varios_productos(self):
        leche = Producto("Leche", 80)
        platano = Producto("Platano", 20)
        self.carrito.agregar_producto(leche, 2)
        self.carrito.agregar_producto(platano, 1)
        self.assertEqual(len(self.carrito.productos), 3)

    def test_agregar_ningun_producto(self):
        soda = Producto("Soda", 25)
        self.carrito.agregar_producto(soda, 0)
        self.assertEqual(len(self.carrito.productos), 0)

    def test_agregar_cantidad_negativa(self):
        soda = Producto("Soda", 25)
        self.assertEqual(
            self.carrito.agregar_producto(soda, -3),
            "Error: No se puede agregar una cantidad negativa de productos al carrito."
        )

    def test_eliminar_producto(self):
        jugo = Producto("Jugo", 26)
        self.carrito.agregar_producto(jugo, 2)
        resp = self.carrito.eliminar_producto(jugo)
        self.assertEqual(resp, "Producto Jugo eliminado del carrito.")
        self.assertEqual(len(self.carrito.productos), 1)

    def test_eliminar_producto_no_existente(self):
        jugo = Producto("Jugo", 26)
        self.carrito.agregar_producto(jugo, 1)
        helado = Producto("Helado", 50)
        self.assertEqual(
            self.carrito.eliminar_producto(helado),
            "El producto Helado no está en el carrito."
        )

    def test_eliminar_producto_carrito_vacio(self):
        helado = Producto("Helado", 50)
        self.assertEqual(
            self.carrito.eliminar_producto(helado),
            "El carrito está vacío. No se puede eliminar ningún producto."
        )

    def test_calcular_subtotal(self):
        pan = Producto("Pan", 45)
        huevos = Producto("Huevos", 35)
        self.carrito.agregar_producto(pan, 3)
        self.carrito.agregar_producto(huevos, 2)
        self.assertEqual(self.carrito.calcular_subtotal(), 205)

    def test_aplicar_descuento_al_total(self):
        brocoli = Producto("Brocoli", 25)
        tomate = Producto("Tomate", 40)
        self.carrito.agregar_producto(brocoli, 2)
        self.carrito.agregar_producto(tomate, 5)
        total_con_descuento = self.carrito.calcular_total_con_descuento(descuento=0.10)
        self.assertAlmostEqual(total_con_descuento, 261, delta=1)

    def test_manejar_carrito_vacio(self):
        subtotal = self.carrito.calcular_subtotal()
        total = self.carrito.calcular_total_con_descuento()
        self.assertEqual(subtotal, 0)
        self.assertEqual(total, 0)
