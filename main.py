import conexion
from ingredinetes import Productos
print("bienvenidos")
print("si desea ingresar datos precione 1")

dato = int(input("ingresa el numero"))

if dato == 1:
    con = conexion.BaseDeDatos()
    idproducto = int(input("ingresa el codigo"))
    nombre = input("ingresa el nombre del producto")
    descripcion = input("producto")
    precio = int(input("ingrese el precio"))
    idingredientes = int(input("ingrese codigo de ingredintes"))

    datos = Productos(idproducto, nombre, descripcion, precio, idingredientes)
    con.insertar_productos(datos)
elif dato == 2:
    cone = conexion.BaseDeDatos()
    conee = cone.Listado_De_Productos()
    for i in conee:
        print("id producto: " , i[0] , "Nombre: " , i[1] , "Descripcion" , i[2], "Precio: " , i[3] , "id ingredientes" , i[4])