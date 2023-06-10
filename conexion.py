import mysql.connector #importamos la libreria

class BaseDeDatos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                port = 3306,
                password = "pancho1677",
                database = "bigbread"
            )
            if self.conexion.is_connected:
                print("conexion exitosa")
                
        except mysql.connector.Error() as error:
            print("a ocurrido este error: ", error)

    def insertar_productos(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sentenciaSql = "INSERT INTO productos values(%s, %s, %s, %s, %s)"
                print("estoy aqui")               
                data = (a.getid_producto(),
                         a.getnombre(),
                         a.getdescripcion(),
                         a.getprecio(),
                         a.getid_ingredientes()
                         )
                
                
                cursor.execute(sentenciaSql, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as error:
                print("a ocurrido este error: ", error)


    def Listado_De_Productos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de mostrar los datos: ", error)

