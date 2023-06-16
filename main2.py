import controlador as con

print("bienvenidos")

while True:
    print("si desea ver lista de productos presione 1 ")
    print("")
    print("si desea ver lista de ingredientes presione 2 ")
    print("")
    print("si desea ingresar datos de ingredientes presione 3 ")
    print("")
    print("si desea ingresar datos de productos presione 4 ")
    print("")
    print("si desea eliminar un producto presiona 5 ")
    print("")
    print("si desea eliminar un ingrediente presiona 6 ")
    print("")
    print("si desea actualizar precio del producto presiona 7 ")
    print("")
    print("si desea actualizar descripcion de ingrediente presiona 8 ")
    print("")
    print("si desea salir del programa presione 9")

    numero = int(input("ingrese numero:  "))
    if numero == 1:
        con.verProductos()
    if numero == 2:
        con.verIngredientes()
    if numero == 3:
        con.insertarIngredientes()
    if numero == 4:
        con.insertarProductos()
    if numero == 5:
        con.eliminarProducto()
    if numero == 6:
        con.eliminarIngredientes()
    if numero == 7:
        con.actualizarProducto()
    if numero == 8:
        con.actualizarIngredientes()
    if numero == 9:
        break
    else:
        print("ingreso un numero invalido vuelva a ingresar")
        print("")
        print("")


