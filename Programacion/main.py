import controlador as con

print("--------------------Bienvenido a BigBread-------------------")
print("")

while True: 
    print("--------------------| Menu |-------------------") #interfaz grafca del programa
    print("")
    print("-----!seleccione una opcion para continuar!-----")
    print("")
    print("-----------------| 1 |  productos |-----------------")
    print("")
    print("-----------------| 2 |  ingredientes |-----------------")
    print("")
    print("-----------------| 3 | salir |-----------------")
    print("")
    print("")

    numero = int(input("ingrese numero:  "))

    if numero == 1:
        print("--------------------| Menu Productos |-------------------")
        print("")
        print("---| 1 |--- ver lista de productos")
        print("")
        print("---| 2 |--- ingresar datos de productos")
        print("")
        print("---| 3 |--- eliminar un producto")
        print("")
        print("---| 4 |--- actualizar precio de producto")
        print("")
        print("---| 5 |--- salir del programa")
        print("")
        print("")

        produnumero = int(input("ingrese numero:  "))

        if produnumero == 1:
            con.verProductos()
        elif produnumero == 2:
            con.insertarProductos()
        elif produnumero == 3:
            con.eliminarProducto()
        elif produnumero == 4:
            con.actualizarProducto()
        elif produnumero == 5:
            print("--------------------| Gracias por usar BigBread |-------------------")
            break
        else:
            print("ingreso un numero invalido vuelva a ingresar")
            print("")
            print("")

    elif numero == 2:
        print("--------------------| Menu Ingredientes |-------------------")
        print("")
        print("---| 1 |--- ver lista de ingredientes ")
        print("")   
        print("---| 2 |--- ingresar datos de ingredientes")
        print("")
        print("---| 3 |--- eliminar un ingrediente")
        print("")
        print("---| 4 |--- actualizar precio de ingrediente")
        print("")
        print("---| 5 |--- salir del programa")
        print("")
        print("")


        ingrenumero = int(input("ingrese numero:  "))

        if ingrenumero == 1:
            con.verIngredientes()
        elif ingrenumero == 2:
            con.insertarIngredientes()
        elif ingrenumero == 3:
            con.eliminarIngredientes()
        elif ingrenumero == 4:
            con.actualizarIngredientes()
        elif ingrenumero == 5:
            print("--------------------| Gracias por usar BigBread |-------------------")
            break
        else:
            print("ingreso un numero invalido vuelva a ingresar")
            print("")
            print("")
    elif numero == 3:
        print("--------------------| Gracias por usar BigBread |-------------------")
        print("")
        break

    else:
        print("ingreso un numero invalido vuelva a ingresar")
        print("")
        print("")



    # if numero == 1:
    #     con.verProductos()
    # if numero == 2:
    #     con.verIngredientes()
    # if numero == 3:
    #     con.insertarIngredientes()
    # if numero == 4:
    #     con.insertarProductos()
    # if numero == 5:
    #     con.eliminarProducto()
    # if numero == 6:
    #     con.eliminarIngredientes()
    # if numero == 7:
    #     con.actualizarProducto()
    # if numero == 8:
    #     con.actualizarIngredientes()
    # if numero == 9:
    #     break
    # else:
    #     print("ingreso un numero invalido vuelva a ingresar")
    #     print("")
    #     print("")


