from classBD import conectar_base_datos

class Producto():
    Id_producto = 0
    Nombre = ""
    Descripcion = ""
    Precio = 0

    def __init__(self, id_producto, nombre, descripcion, precio):
        self.Id_producto = id_producto
        self.Nombre = nombre
        self.Descripcion = descripcion
        self.Precio = precio

