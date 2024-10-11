-- Insertar una biblioteca
INSERT INTO Biblioteca (nombre, ubicacion) 
VALUES ('Biblioteca Central', 'Avenida Siempre Viva 123');

-- Insertar 10 libros
INSERT INTO Libro (titulo, autor, isbn) 
VALUES 
('Cien Años de Soledad', 'Gabriel García Márquez', '9780307474728'),
('1984', 'George Orwell', '9780451524935'),
('El Principito', 'Antoine de Saint-Exupéry', '9788498381493'),
('Don Quijote de la Mancha', 'Miguel de Cervantes', '9788491051959'),
('Fahrenheit 451', 'Ray Bradbury', '9781451673319'),
('Matar a un Ruiseñor', 'Harper Lee', '9780060935467'),
('La Odisea', 'Homero', '9780140268867'),
('Crimen y Castigo', 'Fiódor Dostoyevski', '9780140449136'),
('El Gran Gatsby', 'F. Scott Fitzgerald', '9780743273565'),
('La Divina Comedia', 'Dante Alighieri', '9780140448955');

-- Insertar 20 usuarios
INSERT INTO Usuario (rut, nombre) 
VALUES 
('12345678-1', 'Ana González'),
('12345678-2', 'Luis Pérez'),
('12345678-3', 'María Sánchez'),
('12345678-4', 'Carlos Hernández'),
('12345678-5', 'Patricia López'),
('12345678-6', 'Ricardo Ramírez'),
('12345678-7', 'Gabriela Torres'),
('12345678-8', 'Jorge Ortiz'),
('12345678-9', 'Sandra Jiménez'),
('12345678-10', 'Francisco Medina'),
('12345678-11', 'Lucía Castro'),
('12345678-12', 'Miguel Morales'),
('12345678-13', 'Andrea Muñoz'),
('12345678-14', 'David Fernández'),
('12345678-15', 'Laura Silva'),
('12345678-16', 'Fernando Rojas'),
('12345678-17', 'Natalia Vargas'),
('12345678-18', 'José Gutiérrez'),
('12345678-19', 'Elena Guerrero'),
('12345678-20', 'Manuel Cruz');

-- Insertar 20 préstamos con fechas realistas (algunos devueltos, otros aún prestados)
INSERT INTO Prestamo (libro_id, usuario_rut, fecha_prestamo, fecha_devolucion)
VALUES
(1, '12345678-1', '2024-09-01', '2024-09-15'),
(2, '12345678-2', '2024-09-05', '2024-09-19'),
(3, '12345678-3', '2024-09-07', '2024-09-21'),
(4, '12345678-4', '2024-09-08', '2024-09-22'),
(5, '12345678-5', '2024-09-10', '2024-09-24'),
(6, '12345678-6', '2024-09-11', '2024-09-25'),
(7, '12345678-7', '2024-09-12', '2024-09-26'),
(8, '12345678-8', '2024-09-13', '2024-09-27'),
(9, '12345678-9', '2024-09-14', '2024-09-28'),
(10, '12345678-10', '2024-09-15', '2024-09-29'),
(1, '12345678-11', '2024-09-16', '2024-09-30'),
(2, '12345678-12', '2024-09-17', '2024-10-01'),
(3, '12345678-13', '2024-09-18', '2024-10-02'),
(4, '12345678-14', '2024-09-19', '2024-10-03'),
(5, '12345678-15', '2024-09-20', '2024-10-04'),
(6, '12345678-16', '2024-09-21', '2024-10-05'),
(7, '12345678-17', '2024-09-22', '2024-10-06'),
(8, '12345678-18', '2024-09-23', '2024-10-07'),
(9, '12345678-19', '2024-09-24', NULL), -- Aún no devuelto
(10, '12345678-20', '2024-09-25', NULL); -- Aún no devuelto
