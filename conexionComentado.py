import mysql.connector #importamos la libreria

class BaseDeDatos(): #creamos la clase
    def __init__(self) -> None: #creamos el constructor
        try: #creamos un try para verificar si la conexion fue exitosa
            self.conexion = mysql.connector.connect( #creamos la conexion
                host = "localhost", # pasamos los datos de la conexion
                user = "root",
                port = 3306,
                password = "pancho1677",
                database = "bigbread"
            )
            if self.conexion.is_connected: #verificamos si la conexion fue exitosa
                print("conexion exitosa")
                
        except mysql.connector.Error() as error: #si la conexion no fue exitosa, nos mostrara el error
            print("a ocurrido este error: ", error)

    def insertar_productos(self, a): #creamos el metodo para insertar datos
        if self.conexion.is_connected: #verificamos si la conexion esta activa
            try: 
                cursor = self.conexion.cursor() #creamos el cursor que sirve para ejecutar las sentencias sql
                sentenciaSql = "INSERT INTO productos values(%s, %s, %s, %s, %s)" #creamos la sentencia sql               
                data = (a.getid_producto(), #creamos una tabla con los datos que vamos a insertar
                         a.getnombre(),
                         a.getdescripcion(),
                         a.getprecio(),
                         a.getid_ingredientes()
                         )
                
                
                cursor.execute(sentenciaSql, data) #ejecutamos la sentencia sql y le pasamos los datos
                self.conexion.commit() #commit para guardar los datos en la base de datos
                self.conexion.close() #cerramos la conexion
            except mysql.connector.Error as error:  #si la conexion no fue exitosa, nos mostrara el error
                print("a ocurrido este error: ", error) 


    def Listado_De_Productos(self): #creamos el metodo para mostrar los datos
        if self.conexion.is_connected(): 
            try:
                cursor = self.conexion.cursor() #creamos el cursor que sirve para ejecutar las sentencias sql
                sentenciaSQL = "SELECT * FROM productos"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall() #fetchall para mostrar todos los datos de la tabla
                if len(resultados) < 1: #verificamos si hay datos en la tabla
                    print("")
                    print("---| no hay datos para mostrar |---")
                self.conexion.close() #cerramos la conexion
                return resultados #retornamos los datos
            
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de mostrar los datos: ", error)
    
    def ListadoIngredientes(self): #creamos el metodo para mostrar los datos
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM ingredientes"
                cursor.execute(sentenciaSQL)
                resultados= cursor.fetchall() #fetchall sirve para mostrar todos los datos de la tabla
                if len(resultados) < 1: #verificamos si hay datos en la tabla
                    print("")
                    print("---| no hay datos para mostrar |---")
                self.conexion.close()
                return resultados #retornamos los datos
            
            except mysql.connector.Error as error:
                print("a ocurrido este error al tratar de mostrar los datos: ", error)

    def insertarIngredientes(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO ingredientes values(%s,%s,%s)" #creamos la sentencia sql
                data = (a.getid_ingredientes(), #creamos una tabla con los datos que vamos a insertar
                        a.getnombre(),
                        a.getdescripcion())
                cursor.execute(sql, data) #ejecutamos la sentencia sql y le pasamos los datos
                self.conexion.commit() #commit para guardar los datos en la base de datos
                self.conexion.close()
            except mysql.connector.Error() as error:
                print("el error es: " , error)

    def eliminarProducto(self, a):
        if self.conexion.is_connected: #verificamos si la conexion esta activa
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM productos where id_producto = %s"%a #creamos la sentencia sql para eliminar productos	
                cursor.execute(sql) #ejecutamos la sentencia sql
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error() as Error:
                print("el error es el siguiente: ", Error)
    def eliminarIngredientes(self, a):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM ingredientes WHERE id_ingrediente = %s"%a #creamos la sentencia sql para eliminar ingredientes
                cursor.execute(sql)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error() as Error:
                print("el error es el siguiente: ", Error)

    def actualizarProdcutos(self,a ,b):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql ="UPDATE productos SET precio ='%s' WHERE id_producto = %i" % (b, int(a)) # b toma posicion de valor del precio y a toma posicion del id_producto
                cursor.execute(sql) #ejecutamos la sentencia sql
                self.conexion.commit() #commit para guardar los datos en la base de datos
                self.conexion.close()
                print("actualizado correctamente")

            except mysql.connector.Error() as error:
                print("el error es :",error )

    def actualizarIngredientes(self,a, b):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE ingredientes SET descripcion ='%s' WHERE nombre = '%s'" % (b, a) # b toma posicion de valor de la descripcion y a toma posicion del nombre
                cursor.execute(sql)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error() as error:
                print("el error es: ", error)


""" pasos para crear una base de datos en mysql
    1. crear la base de datos (create database nombre_de_la_base_de_datos)
    2. crear las tablas  (create table nombre_de_la_tabla)
    3. crear los campos de las tablas (create table nombre_de_la_tabla (nombre_del_campo tipo_de_dato))
    4. crear las relaciones entre las tablas (create table nombre_de_la_tabla (nombre_del_campo tipo_de_dato, foreign key (nombre_del_campo) references nombre_de_la_tabla(nombre_del_campo)))
    5. crear los datos de prueba (insert into nombre_de_la_tabla values (datos_de_prueba))

    6. crear el codigo para la conexion a la base de datos 
    7. crear el codigo para insertar datos 
    8. crear el codigo para mostrar datos
    9. crear el codigo para eliminar datos
    10. crear el codigo para actualizar datos
    11. crear el codigo para cerrar la conexion
    12. crear el codigo para cerrar el programa
    
    
    pasos para hacer una conexion a mysql desde python
    1. importar la libreria mysql.connector
    2. crear la conexion
    3. crear el cursor para ejecutar las sentencias sql
    4. crear la sentencia sql que queremos ejecutar  (insert, select, update, delete)
    5. ejecutar la sentencia sql con el cursor creado 
    6. cerrar la conexion 
    7. cerrar el programa

    pasos para insertar datos en una tabla
    1. crear la sentencia sql
    2. crear una tabla con los datos que vamos a insertar
    3. ejecutar la sentencia sql con el cursor creado
    4. conexion.commit() para guardar los datos en la base de datos
    5. conexion.close() para cerrar la conexion


    conexion = mysql.connector.connect() para crear la conexion
    cursor = conexion.cursor() para crear el cursor que sirve para ejecutar las sentencias sql
    sentenciaSQL = "SELECT * FROM productos" para crear la sentencia sql que queremos ejecutar
    cursor.execute(sentenciaSQL) para ejecutar la sentencia sql 
    conexion.commit() para guardar los datos en la base de datos
    conexion.close() para cerrar la conexion
    cursor.execute() para ejecutar la sentencia sql
    cursor.fetchall() para mostrar todos los datos de la tabla
    cursor.fetchone() para mostrar un solo dato de la tabla
    cursor.fetchmany() para mostrar varios datos de la tabla


    CREATE DATABASE BigBread; esto es para crear la base de datos

use bigbread;  esto es para usar la base de datos


CREATE TABLE Productos (                                  esto es para crear la tabla de productos
  id_producto INT PRIMARY KEY AUTO_INCREMENT,             esto es para crear el id de la tabla
  nombre VARCHAR(100) NOT NULL,                           varchar es para crear un campo de texto y not null es para que el campo no este vacio
  descripcion VARCHAR(255),                        
  precio DECIMAL(10, 2) NOT NULL,                         decimal es para crear un campo de numeros 
  id_ingredientes int not null FOREIGN KEY                foreign key es para crear una relacion entre tablas
);

-- Crear tabla de ingredientes                             
CREATE TABLE Ingredientes ( 
  id_ingrediente INT PRIMARY KEY AUTO_INCREMENT,          primary key es para crear el id de la tabla y auto_increment es para que el id se auto incremente
  nombre VARCHAR(100) NOT NULL,                           
  descripcion VARCHAR(255)
);

    """