import mysql.connector
from mysql.connector import Error

class Libro:
    def __init__(self, id, titulo, autor, isbn, disponibilidad=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = disponibilidad

class Usuario:
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

class BibliotecaModel:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_libros(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM Libro")
            libros = cursor.fetchall()
            return libros
        except Error as e:
            print(f"Error al obtener los libros: {e}")
        finally:
            cursor.close()

    def registrar_usuario(self, rut, nombre):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("INSERT INTO Usuario (rut, nombre) VALUES (%s, %s)", (rut, nombre))
            self.conexion.commit()
        except Error as e:
            print(f"Error al registrar usuario: {e}")
        finally:
            cursor.close()

    def prestar_libro(self, libro_id, rut_usuario):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT disponibilidad FROM Libro WHERE id = %s", (libro_id,))
            disponibilidad = cursor.fetchone()[0]
            if disponibilidad:
                cursor.execute("UPDATE Libro SET disponibilidad = 0 WHERE id = %s", (libro_id,))
                cursor.execute("INSERT INTO Prestamo (libro_id, usuario_rut, fecha_prestamo) VALUES (%s, %s, CURDATE())", (libro_id, rut_usuario))
                self.conexion.commit()
            else:
                return False
        except Error as e:
            print(f"Error al prestar el libro: {e}")
        finally:
            cursor.close()
        return True

    def devolver_libro(self, libro_id, rut_usuario):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT id FROM Prestamo WHERE libro_id = %s AND usuario_rut = %s AND fecha_devolucion IS NULL", (libro_id, rut_usuario))
            prestamo = cursor.fetchone()
            if prestamo:
                cursor.execute("UPDATE Prestamo SET fecha_devolucion = CURDATE() WHERE id = %s", (prestamo[0],))
                cursor.execute("UPDATE Libro SET disponibilidad = 1 WHERE id = %s", (libro_id,))
                self.conexion.commit()
            else:
                return False
        except Error as e:
            print(f"Error al devolver el libro: {e}")
        finally:
            cursor.close()
        return True
