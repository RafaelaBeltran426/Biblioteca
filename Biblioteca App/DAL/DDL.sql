-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS biblioteca;

-- Usar la base de datos creada
USE biblioteca;

-- Crear la tabla Libro si no existe
CREATE TABLE IF NOT EXISTS Libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    isbn VARCHAR(13) UNIQUE NOT NULL,
    disponibilidad BOOLEAN DEFAULT TRUE
);

-- Crear la tabla Usuario si no existe
CREATE TABLE IF NOT EXISTS Usuario (
    rut VARCHAR(12) PRIMARY KEY,  -- RUT como identificador único
    nombre VARCHAR(255) NOT NULL
);

-- Crear la tabla Biblioteca si no existe (si se requiere manejar varias bibliotecas)
CREATE TABLE IF NOT EXISTS Biblioteca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL
);

-- Crear la tabla Prestamo si no existe (relación entre Usuario y Libro)
CREATE TABLE IF NOT EXISTS Prestamo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    libro_id INT,
    usuario_rut VARCHAR(12),
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    FOREIGN KEY (libro_id) REFERENCES Libro(id),
    FOREIGN KEY (usuario_rut) REFERENCES Usuario(rut)
);