import conexion 
from productos import Productos
from ingredientes import Ingredientes

def verProductos():
    conec = conexion.BaseDeDatos()
    print("\n| ID PRODUCTO  |  NOMBRE PRODUCTO  |  DESCRIPCION  |  PRECIO  |  ID INGREDIENTE"  )
    lista = conec.Listado_De_Productos()
    for i in lista: #se crea un for para recorrer la lista de los datos
            print("----------------------------------")
            print("")
            print("---|""ID PRODUCTO      |" ,i[0])
            print("---|""NOMBRE PRODUCTO  |" ,i[1])
            print("---|""DESCRIPCION      |" ,i[2])
            print("---|""PRECIO           |" ,i[3])
            print("---|""ID INGREDIENTE   |" ,i[4])
            print("")

    print("")
    input("presione enter para continuar")
    print("")
    

def verIngredientes():
     conec = conexion.BaseDeDatos()
     print("\n| ID INGREDIENTE  |  NOMBRE  |  DESCRIPCION  |")
     lista = conec.ListadoIngredientes()
     for i in lista:
           print("----------------------------------")
           print("")
           print("---| ID INGREDIENTE   |",i[0])
           print("---| NOMBRE           |",i[1])
           print("---| DESCRIPCION      |",i[2])
     print("")
     input("presione enter para continuar")
     print("")


def insertarProductos():
     conec = conexion.BaseDeDatos()
     id_producto = int(input("--|ingrese id del producto: |--"))
     nombre = input("--|ingrese el nombre del producto: |--")
     descripcion = input("--|ingrese descripcion: |--")
     precio = input("--|ingrese el precio: |--")
     id_ingrediente = input("--|ingrese id del ingrediente:  |--")
     dato = Productos(id_producto, nombre, descripcion, precio,  id_ingrediente)
     conec.insertar_productos(dato)
     print("")
     print("producto agregado con exito")
     input("presione enter para continuar")
     print("")
     
    
def insertarIngredientes():
     conec = conexion.BaseDeDatos()
     id_ingredinetes = int(input("--|ingrese id de los ingredietes: |--"))
     nombre = input("--|ingresar nombre: |--")
     descripcion = input("--|ingrese descripcion: |--")
     dato = Ingredientes(id_ingredinetes, nombre, descripcion)
     conec.insertarIngredientes(dato)
     print("")
     print("ingrediente agregado con exito")
     input("presine enter para continuar")
     print("")
     

def eliminarProducto():
     cone = conexion.BaseDeDatos()
     verProductos()
     id = int(input("--|ingrese el id del producto que desea eliminar: |-- "))
     cone.eliminarProducto(id)
     print("")
     print("producto eliminado con exito")
     input ("presiona enter para continuar")
     print("")

    
def eliminarIngredientes():
     cone = conexion.BaseDeDatos()
     verIngredientes()
     id = int(input("--|ingrese id del ingrediente que desa eliminar: |--"))
     cone.eliminarIngredientes(id)
     print("")
     print("ingrediente eliminado con exito")
     input("presiones enter para continuar")
     print("")
     

def actualizarProducto():
     cone = conexion.BaseDeDatos()
     id = int (input("--|ingrese el id del producto a modificar: |--"))
     precio = int(input("--|ingrese el nuevo precio: |--"))
     cone.actualizarProdcutos(id, precio)
     print("")
     print("producto actualizado con exito")
     input("presione enter para continuar")
     print("")
     

def actualizarIngredientes():
    cone = conexion.BaseDeDatos()
    nombre = input("ingrese el id a actualizar ")
    descripcion = input("ingrese nueva descripcion ")
    cone.actualizarIngredientes(nombre, descripcion)
    print("")
    print("ingrediente actualizado con exito")
    input("presiones enter para continuar")
    print("")
    
