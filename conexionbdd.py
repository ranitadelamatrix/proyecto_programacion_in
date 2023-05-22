import mysql.connector  #escribimos para iportar base de dadatos

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pancho1677",
        database="BigBread",
        )

    if connection.is_connected():
            print("exitosa")
    else:
        print("no se conecto")

finally:
    if connection.is_connected():
       connection.close()
       print("cerrado")