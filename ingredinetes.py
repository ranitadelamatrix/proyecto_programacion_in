class Productos():
    id_producto = 0
    nombre = ""
    descripcion = ""
    precio = 0
    id_ingredientes = 0

    def __init__(self, id_producto, nombre, descripcion, precio, id_ingredientes) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.id_ingredientes = id_ingredientes

    def getid_producto(self):
        return self.id_producto
    def getnombre(self):
        return self.nombre
    def getdescripcion(self):
        return self.descripcion
    def getprecio(self):
        return self.precio
    def getid_ingredientes(self):
        return self.id_ingredientes
    
    def setid_producto(self, id_producto):
        self.id_producto = id_producto
    def setnombre(self, nombre):
        self.nombre = nombre
    def setdescripcion(self, descripcion):
        self.descripcion = descripcion
    def setprecio(self, precio):
        self.precio = precio
    def setid_ingredientes(self, id_ingredientes):
        self.id_ingredientes = id_ingredientes
