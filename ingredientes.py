class Productos(): #se crea la clase productos
    id_producto = 0 #se crean las variables de la clase productos
    nombre = ""
    descripcion = ""
    precio = 0
    id_ingredientes = 0

    def __init__(self, id_producto, nombre, descripcion, precio, id_ingredientes) -> None: #se crea el constructor de la clase productos
        self.id_producto = id_producto #se asignan los valores a las variables d
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.id_ingredientes = id_ingredientes

    def getid_producto(self): #se crean los metodos get y set de la clase productos
        return self.id_producto
    def getnombre(self):
        return self.nombre
    def getdescripcion(self):
        return self.descripcion # se retorna los valores de las variables
    def getprecio(self):
        return self.precio
    def getid_ingredientes(self):
        return self.id_ingredientes
    
    def setid_producto(self, id_producto): 
        self.id_producto = id_producto #se asignan los valores a las variables
    def setnombre(self, nombre):
        self.nombre = nombre
    def setdescripcion(self, descripcion):
        self.descripcion = descripcion
    def setprecio(self, precio):
        self.precio = precio
    def setid_ingredientes(self, id_ingredientes):
        self.id_ingredientes = id_ingredientes


class ingredientes(): #se crea la clase ingredientes
    id_ingredientes = 0 #se crean las variables de la clase ingredientes
    nombre = ""
    descripcion = ""

    def __init__(self, id_ingredientes, nombre, descripcion) -> None: #se crea el constructor de la clase ingredientes
        self.id_ingredientes = id_ingredientes
        self.nombre = nombre
        self.descripcion = descripcion

    def getid_ingredientes(self):
        return self.id_ingredientes
    def getnombre(self):
        return self.nombre
    def getdescripcion(self):
        return self.descripcion

    def setid_ingredientes(self, id_ingredientes):
        self.id_ingredientes = id_ingredientes
    def setnombre(self, nombre):
        self.nombre = nombre
    def setdescripcion(self, descripcion):
        self.descripcion = descripcion