

class Ingredientes():
    id_ingredientes = 0
    nombre = ""
    descripcion = ""

    def __init__(self, id_ingredintes, nombre, descripcion) -> None:
        self.id_ingredientes = id_ingredintes
        self.nombre = nombre
        self.descripcion = descripcion
    
    def getid_ingredientes(self):
        return self.id_ingredientes
    def getnombre(self):
        return self.nombre
    def getdescripcion(self):
        return self.descripcion
    
    def setid_ingredientes(self, id_ingredintes):
        self.id_ingredientes = id_ingredintes
    def setnombre(self, nombre):
        self.nombre = nombre
    def setdescripcion(self, descripcion):
        self.descripcion = descripcion

    

        