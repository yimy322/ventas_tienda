class Producto:
    def __init__(self, id_producto, nombre, categoria, fecha, precio, unidades):
        self.id = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.fecha = fecha
        self.precio = float(precio)
        self.unidades = int(unidades)

    def total_venta(self):
        return self.precio * self.unidades
