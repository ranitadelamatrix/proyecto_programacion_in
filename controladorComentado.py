import conexion  #importamos la conexion de la base de datos
from ingredientes import Productos  #importamos la clase productos
from ingredientes import Ingredientes  #importamos la clase ingredientes

def verProductos(): #se crea una funcion para ver los productos
    conec = conexion.BaseDeDatos() #se crea una variable para la conexion
    print("\n| ID PRODUCTO  |  NOMBRE PRODUCTO  |  DESCRIPCION  |  PRECIO  |  ID INGREDIENTE"  ) #se imprime el encabezado de la tabla
    lista = conec.Listado_De_Productos() #se crea una variable para la lista de los productos que trae los datos
    for i in lista: #se crea un for para recorrer la lista de los datos
            print("----------------------------------")
            print("")
            print("---|""ID PRODUCTO      |" ,i[0]) #se imprime los datos de la lista
            print("---|""NOMBRE PRODUCTO  |" ,i[1])
            print("---|""DESCRIPCION      |" ,i[2])
            print("---|""PRECIO           |" ,i[3])
            print("---|""ID INGREDIENTE   |" ,i[4])
            print("")

    print("")
    input("presione enter para continuar") #se imprime un mensaje para continuar  debido que al estar en un bucle no llegamos a ver los datos
    print("")
    

def verIngredientes(): #se crea una funcion para ver los ingredientes
     conec = conexion.BaseDeDatos()  #se crea una variable para la conexion
     print("\n| ID INGREDIENTE  |  NOMBRE  |  DESCRIPCION  |") #se imprime el encabezado de la tabla
     lista = conec.ListadoIngredientes() #se crea una variable para la lista de los ingredientes que trae los datos
     for i in lista: #se crea un for para recorrer la lista de los datos
           print("----------------------------------")
           print("")
           print("---| ID INGREDIENTE   |",i[0]) #se imprime los datos de la lista
           print("---| NOMBRE           |",i[1])
           print("---| DESCRIPCION      |",i[2])
     print("")
     input("presione enter para continuar") #se imprime un mensaje para continuar  debido que al estar en un bucle no llegamos a ver los datos
     print("")


def insertarProductos(): #se crea una funcion para insertar los productos
     conec = conexion.BaseDeDatos() #se crea una variable para la conexion
     id_producto = int(input("--|ingrese id del producto: |--")) #se crea una variable para el id del producto
     nombre = input("--|ingrese el nombre del producto: |--")
     descripcion = input("--|ingrese descripcion: |--")
     precio = input("--|ingrese el precio: |--")
     id_ingrediente = input("--|ingrese id del ingrediente:  |--")
     dato = Productos(id_producto, nombre, descripcion,  precio,  id_ingrediente) #se crea una variable para los datos de los productos que se van a insertar que vienen de la clase productos
     conec.insertar_productos(dato)  #se crea una variable para la conexion y se insertan los datos de los productos
     print("")
     print("producto agregado con exito")
     input("presione enter para continuar")
     print("")
     
    
def insertarIngredientes(): #se crea una funcion para insertar los ingredientes
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
     

def eliminarProducto(): #se crea una funcion para eliminar los productos
     cone = conexion.BaseDeDatos()
     verProductos() #se llama a la funcion ver productos para ver los productos que hay
     id = int(input("--|ingrese el id del producto que desea eliminar: |-- "))
     cone.eliminarProducto(id) #se crea una variable para la conexion y se elimina el producto
     print("")
     print("producto eliminado con exito")
     input ("presiona enter para continuar")
     print("")

    
def eliminarIngredientes(): #se crea una funcion para eliminar los ingredientes
     cone = conexion.BaseDeDatos() #se crea una variable para la conexion
     verIngredientes()
     id = int(input("--|ingrese id del ingrediente que desa eliminar: |--")) #se crea una variable para el id del ingrediente
     cone.eliminarIngredientes(id) #se crea una variable para la conexion y se elimina el ingrediente
     print("")
     print("ingrediente eliminado con exito")
     input("presiones enter para continuar")
     print("")
     

def actualizarProducto(): #se crea una funcion para actualizar los productos
     cone = conexion.BaseDeDatos() #se crea una variable para la conexion
     id = int (input("--|ingrese el id del producto a modificar: |--")) #se crea una variable para el id del producto
     precio = int(input("--|ingrese el nuevo precio: |--"))
     cone.actualizarProdcutos(id, precio) #se crea una variable para la conexion y se actualiza el precio del producto
     print("")
     print("producto actualizado con exito")
     input("presione enter para continuar")
     print("")
     

def actualizarIngredientes(): #se crea una funcion para actualizar los ingredientes
    cone = conexion.BaseDeDatos() #se crea una variable para la conexion
    nombre = input("ingrese el id a actualizar ") #se crea una variable para el nombre del ingrediente
    descripcion = input("ingrese nueva descripcion ") #se crea una variable para la descripcion del ingrediente
    cone.actualizarIngredientes(nombre, descripcion) #se crea una variable para la conexion y se actualiza la descripcion del ingrediente
    print("")
    print("ingrediente actualizado con exito")
    input("presiones enter para continuar")
    print("")
    
