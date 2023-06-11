import mysql.connector #importamos la libreria

class BaseDeDatos(): #se crea la clase conexion
    def __init__(self) -> None: #se crea el constructor de la clase conexion
        try:
            self.conexion = mysql.connector.connect( #se crea la conexion con la base de datos con las credenciales 
                host = "localhost",
                user = "root",
                port = 3306,
                password = "pancho1677",
                database = "bigbread"
            )
            if self.conexion.is_connected: #se verifica si la conexion fue exitosa
                print("conexion exitosa")
                
        except mysql.connector.Error() as error: #se crea una excepcion para verificar si la conexion fue exitosa
            print("a ocurrido este error: ", error)

    def insertar_productos(self, a): #se crea el metodo insertar_productos
        if self.conexion.is_connected: 
            try:
                cursor = self.conexion.cursor() #se crea un cursor para ejecutar las sentencias sql
                sentenciaSql = "INSERT INTO productos values(%s, %s, %s, %s, %s)" #insert sirve para insertar datos en la tabla
            
                data = (a.getid_producto(), #se crea una lista para almacenar los datos
                         a.getnombre(),
                         a.getdescripcion(),
                         a.getprecio(),
                         a.getid_ingredientes()
                         )
                
                
                cursor.execute(sentenciaSql, data) #se ejecuta la sentencia sql y se le pasa la lista con los datos a insertar en la tabla
                self.conexion.commit() #se confirma la sentencia sql
                self.conexion.close() #se cierra la conexion
            except mysql.connector.Error as error:
                    print("a ocurrido este error: ", error)


    def Listado_De_Productos(self): #se crea el metodo Listado_De_Productos para mostrar los datos de la tabla productos
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos" #select * sirve para mostrar todos los datos de la tabla productos
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall() #fetchall retorna una lista con los datos de la tabla
                self.conexion.close()
                return resultados #retorna la lista con los datos de la tabla
            
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de mostrar los datos: ", error)

    def actualizar_productos(self, a):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, id_ingredientes = %s WHERE id_producto = %s" #update sirve para actualizar los datos de la tabla
                data = (a.getnombre(),
                        a.getdescripcion(),
                        a.getprecio(),
                        a.getid_ingredientes(),
                        a.getid_producto()
                        )
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de actualizar los datos: ", error)


    def eliminar_productos(self, a):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM productos WHERE id_producto = %s" #delete sirve para eliminar los datos de la tabla from sirve para indicar de que tabla se van a eliminar los datos
                data = (a.getid_producto(),)
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de eliminar los datos: ", error)



#-----------------------------------------------------ingredientes--------------------------------------------------------------

    def insertar_ingredientes(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sentenciaSql = "INSERT INTO ingredientes values(%s, %s, %s)" #se insertan los datos en la tabla ingredientes
                print("estoy aqui")               
                data = (a.getid_ingredientes(),
                         a.getnombre(),
                         a.getdescripcion()
                         )
                
                
                cursor.execute(sentenciaSql, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as error:
                print("a ocurrido este error: ", error)
    
    def Listado_De_Ingredientes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM ingredientes" #se muestran  todos los datos de la tabla ingredientes
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall()
                self.conexion.close()
                return resultados
            
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de mostrar los datos: ", error)

    def actualizar_ingredientes(self, a):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE ingredientes SET nombre = %s, descripcion = %s WHERE id_ingredientes = %s" #se actualizan los datos de la tabla ingredientes
                data = (a.getnombre(),
                        a.getdescripcion(),
                        a.getid_ingredientes()
                        )
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de actualizar los datos: ", error)

    def eliminar_ingredientes(self, a):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM ingredientes WHERE id_ingredientes = %s" #se eliminan los datos de la tabla ingredientes
                data = (a.getid_ingredientes(),)
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de eliminar los datos: ", error)
