CREATE DATABASE BigBread;

use bigbread; 


CREATE TABLE Productos (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255),
  precio DECIMAL(10, 2) NOT NULL,
  id_ingredientes int not null FOREIGN KEY
);

-- Crear tabla de ingredientes
CREATE TABLE Ingredientes (
  id_ingrediente INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  descripcion VARCHAR(255)
);
