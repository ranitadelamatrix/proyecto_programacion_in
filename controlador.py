import conexion 
from ingredientes import Productos
from ingredientes import Ingredientes

def verProductos():
    conec = conexion.BaseDeDatos()
    lista = conec.Listado_De_Productos()
    for i in lista: #se crea un for para recorrer la lista de los datos
            print("id producto: " , i[0] , "Nombre: " , i[1] , "Descripcion" , i[2], "Precio: " , i[3] , "id ingredientes" , i[4])
    input("presione enter para continuar")

def verIngredientes():
    conec = conexion.BaseDeDatos()
    lista = conec.ListadoIngredientes()
    for i in lista:
        print("id ingredientes: ", i[0], "nombre: ", i[1], "descripcion: ", i [2])
    input("presione enter para continuar")

def insertarProductos():
     conec = conexion.BaseDeDatos()
     id_producto = int(input("ingrese id del producto: "))
     nombre = input("ingrese el nombre del producto: ")
     descripcion = input("ingrese descripcion: ")
     precio = input("ingrese el precio: ")
     id_ingrediente = input("ingrese id del ingrediente: ")
     dato = Productos(id_producto, nombre, descripcion, precio,  id_ingrediente)
     conec.insertar_productos(dato)
     input("presione enter para continuar")
    
def insertarIngredientes():
     conec = conexion.BaseDeDatos()
     id_ingredinetes = int(input("ingrese id de los ingredietes: "))
     nombre = input("ingresar nombre: ")
     descripcion = input("ingrese descripcion: ")
     dato = Ingredientes(id_ingredinetes, nombre, descripcion)
     conec.insertarIngredientes(dato)
     input("presine enter para continuar")

def eliminarProducto():
     cone = conexion.BaseDeDatos()
     id = int(input("ingrese el id del producto que desea eliminar"))
     cone.eliminarProducto(id)
     input ("presiona enter para continuar")
    
def eliminarIngredientes():
     cone = conexion.BaseDeDatos()
     id = int(input("ingrese id del ingrediente que desa eliminar: "))
     cone.eliminarIngredientes(id)
     input("presiones enter para continuar")
def actualizarProducto():
     cone = conexion.BaseDeDatos()
     id = int (input("ingrese el id del producto a modificar:"))
     precio = int(input("ingrese el nuevo precio"))
     cone.actualizarProdcutos(id, precio)
     input("presione enter para continuar")

def actualizarIngredientes():
    cone = conexion.BaseDeDatos()
    nombre = input("ingrese el id a actualizar")
    descripcion = input("ingrese nueva descripcion")
    cone.actualizarIngredientes(nombre, descripcion)
    input("presiones enter para continuar")
