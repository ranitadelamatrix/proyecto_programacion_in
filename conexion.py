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
                if len(resultados) < 1:
                    print("")
                    print("---| no hay datos para mostrar |---")
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de mostrar los datos: ", error)
    
    def ListadoIngredientes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM ingredientes"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                if len(resultados) < 1:
                    print("")
                    print("---| no hay datos para mostrar |---")
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de mostrar los datos: ", error)

    def insertarIngredientes(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO ingredientes values(%s,%s,%s)"
                data = (a.getid_ingredientes(),
                        a.getnombre(),
                        a.getdescripcion())
                cursor.execute(sql, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error() as error:
                print("el error es: " , error)
    def eliminarProducto(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM productos where id_producto = %s"%a
                cursor.execute(sql)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error() as Error:
                print("el error es el siguiente: ", Error)
    def eliminarIngredientes(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM ingredientes WHERE id_ingrediente = %s"%a
                cursor.execute(sql)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error() as Error:
                print("el error es el siguiente: ", Error)

    def actualizarProdcutos(self,a ,b):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql ="UPDATE productos SET precio ='%s' WHERE id_producto = %i" % (b, int(a)) # b toma posicion de valor del precio
                cursor.execute(sql)
                self.conexion.commit()
                self.conexion.close()
                print("actualizado correctamente")

            except mysql.connector.Error() as error:
                print("el error es :",error )

    def actualizarIngredientes(self,a, b):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE ingredientes SET descripcion ='%s' WHERE nombre = '%s'" % (b, a)
                cursor.execute(sql)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error() as error:
                print("el error es: ", error)
