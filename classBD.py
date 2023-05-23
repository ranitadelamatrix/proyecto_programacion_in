import mysql.connector

class conectar_base_datos(): #creamos una clase para poder cnectarnos
    def __init__(self): #inicializamos la clase
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="*******",
                database="grupo_ispc",
            )

            if connection.is_connected():
                print("exitosa")
            else:
                print("no se conecto")

        finally:
                if connection.is_connected():
                    connection.close()
                    print("cerrado")

conexion = conectar_base_datos()