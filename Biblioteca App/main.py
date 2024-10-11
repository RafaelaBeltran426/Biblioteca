import sys
import os

# Agregar el directorio actual al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



from model.models import BibliotecaModel
from view.views import BibliotecaView
from controller.controller import BibliotecaController
import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='biblioteca',  # Nombre de la base de datos
            user='root',  # Cambia el usuario si es necesario
            password=''  # Cambia la contraseña si es necesario
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión: {e}")
        return None

if __name__ == "__main__":
    conexion = conectar()
    if conexion:
        modelo = BibliotecaModel(conexion)
        vista = BibliotecaView()
        controlador = BibliotecaController(modelo, vista)
        controlador.mostrar_menu()
        conexion.close()
