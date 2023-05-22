
CREATE DATABASE BigBread;
USE BigBread;

-- Crear tabla de productos
CREATE TABLE Productos (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255),
  precio DECIMAL(10, 2) NOT NULL
);

-- Crear tabla de ingredientes
CREATE TABLE Ingredientes (
  id_ingrediente INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255)
);

-- Crear tabla de producción
CREATE TABLE Produccion (
  id_produccion INT PRIMARY KEY AUTO_INCREMENT,
  id_producto INT,
  fecha DATE NOT NULL,
  cantidad INT NOT NULL,
  FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

-- Crear tabla de ingredientes utilizados en la producción
CREATE TABLE Ingredientes_Produccion (
  id_produccion INT,
  id_ingrediente INT,
  cantidad DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (id_produccion) REFERENCES Produccion(id_produccion),
  FOREIGN KEY (id_ingrediente) REFERENCES Ingredientes(id_ingrediente)
);

-- Insertar datos en la tabla Productos
INSERT INTO Productos (nombre, descripcion, precio) VALUES
('SANDUCHON', 'Sándwich Venezuela', 5.99),
('FINGER CLUB', 'Sándwich Italian', 7.49),
('TORTA FRIA', 'Sándwich  Braizilian', 6.99),
('SANDWICH DE MIGA', 'Sándwich Argentino', 8.50),
('TRAMEZZINO', 'Sándwich Italian', 7.49),
('TRIPLE SANDWICH', 'Sándwich  Peruvian', 5.50);

-- Insertar datos en la tabla Ingredientes
INSERT INTO Ingredientes (nombre, descripcion) VALUES
  ('Jamón', 'Fiambre de jamón de cerdo'),
  ('Queso', 'Producto lácteo utilizado como ingrediente'),
  ('Pan', 'Base del sándwich'),
  ('Carne empanizada', 'Carne cubierta con pan rallado y frita'),
  ('Lechuga', 'Hojas verdes utilizadas como adorno y saborizante'),
  ('Tomate', 'Fruto utilizado como ingrediente en los sándwiches'),
  ('Mayonesa', 'Salsa cremosa utilizada para aderezar los sándwiches'),
  ('Huevo', 'Huevo cocido utilizado como relleno'),
  ('Bacon', 'Tocino crujiente utilizado para agregar sabor'),
  ('Pepinillos', 'Rodajas de pepinillos encurtidos utilizadas como condimento'),
  ('Cebolla', 'Cebolla en rodajas utilizada para dar sabor'),
  ('Mostaza', 'Salsa de mostaza utilizada como aderezo'),
  ('Aguacate', 'Fruta cremosa utilizada como ingrediente en los sándwiches'),
  ('Salmón', 'Pescado ahumado utilizado como ingrediente'),
  ('Pollo', 'Fiambre de carne de pollo'),
  ('Champiñones', 'Hongos en rodajas utilizados como relleno'),
  ('Aceitunas', 'Aceitunas rellenas utilizadas como adorno y saborizante');

-- Insertar datos en la tabla Produccion
INSERT INTO Produccion (id_producto, fecha, cantidad) VALUES
  (1, '2023-05-20', 50),
  (2, '2023-05-21', 30),
  (3, '2023-05-22', 40),
  (4, '2023-05-23', 35),
  (5, '2023-05-22', 46),
  (6, '2023-05-22', 26);

-- Insertar datos en la tabla Ingredientes_Produccion
INSERT INTO Ingredientes_Produccion (id_produccion, id_ingrediente, cantidad) VALUES
  (1, 1, 5),
  (1, 2, 3),
  (1, 3, 5),
  (2, 2, 4),
  (2, 4, 2),
  (2, 6, 2),
  (3, 3, 4),
  (3, 5, 3),
  (3, 7, 2);

-- Visualizar la lista de productos
SELECT * FROM Productos;

-- Visualizar la lista de ingredientes
SELECT * FROM Ingredientes;

-- Visualizar la cantidad de produccion por dia
SELECT * FROM Produccion;

-- Visualizar ingredientes de produccion
SELECT * FROM Ingredientes_Produccion;