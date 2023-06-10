import conexion #importar la clase conexion
from ingredientes import Productos  #importar la clase productos

con = conexion.BaseDeDatos() #se crea un objeto de la clase conexion

print("**************| Bienvenido a BigBread |**************")
print("-----------------| Menu de opciones |-----------------")
print("-----------------| 1.  productos |-----------------")
print("-----------------| 2.  ingredientes |-----------------")

dato = int(input("ingresa el numero")) #ingresar el numero para la opcion

if dato == 1: 
    print("-----------------| Menu de productos |-----------------")
    print("-----------------| 1.  Ingresar productos |-----------------")
    print("-----------------| 2.  Visualizar productos |-----------------")
    print("-----------------| 3.  Actualizar productos |-----------------")
    print("-----------------| 4.  Eliminar productos |-----------------")
    Productos = int(input("ingresa el numero")) #ingresar el numero para la opcion    




    if Productos == 1: #si el numero es 1 se ejecuta el codigo para ingresar ala tabla de productos
        idproducto = int(input("ingresa el codigo"))
        nombre = input("ingresa el nombre del producto")
        descripcion = input("Agrega una descripcion")
        precio = int(input("ingrese el precio"))
        idingredientes = int(input("ingrese codigo de ingrediente"))

        datos = Productos(idproducto, nombre, descripcion, precio, idingredientes) #se crea un objeto de la clase productos
        con.insertar_productos(datos) #se ejecuta el metodo insertar_productos de la clase conexion

    elif Productos == 2: #si el numero es 2 se ejecuta el codigo para visualizar los productos

        conee = con.Listado_De_Productos() #se ejecuta el metodo Listado_De_Productos de la clase conexion que retorna una lista
        for i in conee: #se crea un for para recorrer la lista de los datos
            print("id producto: " , i[0] , "Nombre: " , i[1] , "Descripcion" , i[2], "Precio: " , i[3] , "id ingredientes" , i[4])

    elif Productos == 3: #si el numero es 3 se ejecuta el codigo para actualizar los productos

        idproducto = int(input("ingresa el codigo"))
        nombre = input("ingresa el nombre del producto")
        descripcion = input("Agrega una descripcion")
        precio = int(input("ingrese el precio"))
        idingredientes = int(input("ingrese codigo de ingrediente"))

        datos = Productos(idproducto, nombre, descripcion, precio, idingredientes) #se crea un objeto de la clase productos
        con.actualizar_productos(datos) #se ejecuta el metodo actualizar_productos de la clase conexion

    elif Productos == 4: #si el numero es 4 se ejecuta el codigo para eliminar los productos
 
        idproducto = int(input("ingresa el codigo"))
        con.eliminar_productos(idproducto) 


elif dato == 2: #si el numero es 2 se ejecuta el codigo para ingresar ala tabla de ingredientes
    print("-----------------| Menu de ingredientes |-----------------")
    print("-----------------| 1.  Ingresar ingredientes |-----------------")
    print("-----------------| 2.  Visualizar ingredientes |-----------------")
    print("-----------------| 3.  Actualizar ingredientes |-----------------")
    print("-----------------| 4.  Eliminar ingredientes |-----------------")
    Ingredientes = int(input("ingresa el numero")) #ingresar el numero para la opcion

    if Ingredientes == 1: #si el numero es 1 se ejecuta el codigo para ingresar ala tabla de ingredientes
        idingredientes = int(input("ingresa el codigo"))
        nombre = input("ingresa el nombre del ingrediente")
        descripcion = input("Agrega una descripcion")

        #datos = ingredientes(idingredientes, nombre, descripcion) 
        con.insertar_ingredientes(datos) #se ejecuta el metodo insertar_ingredientes de la clase conexion
        
    elif Ingredientes == 2: #si el numero es 2 se ejecuta el codigo para visualizar los ingredientes
        
        conee = con.Listado_De_Ingredientes() 
        for i in conee: #se crea un for para recorrer la lista de los datos
            print("id ingredientes: " , i[0] , "Nombre: " , i[1] , "Descripcion" , i[2])

    elif Ingredientes == 3: #si el numero es 3 se ejecuta el codigo para actualizar los ingredientes
        idingredientes = int(input("ingresa el codigo"))
        nombre = input("ingresa el nombre del ingrediente")
        descripcion = input("Agrega una descripcion")

        #datos = ingredientes(idingredientes, nombre, descripcion) 
        con.actualizar_ingredientes(datos) #se ejecuta el metodo actualizar_ingredientes de la clase conexion

    elif Ingredientes == 4: #si el numero es 4 se ejecuta el codigo para eliminar los ingredientes
        idingredientes = int(input("ingresa el codigo"))
        con.eliminar_ingredientes(idingredientes) #se ejecuta el metodo eliminar_ingredientes de la clase conexion

else:
    print("ingresa un numero valido")


