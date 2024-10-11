from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from model.models import BibliotecaModel
import mysql.connector

app = Flask(__name__)
app.secret_key = "mysecretkey"  # Para manejar mensajes flash (opcional)

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='biblioteca',
            user='root',
            password=''
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

conexion = conectar()
biblioteca_model = BibliotecaModel(conexion)

@app.route('/')
def index():
    libros = biblioteca_model.obtener_libros()
    return render_template('index.html', libros=libros)

@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    if request.method == 'POST':
        rut = request.form['rut']
        nombre = request.form['nombre']
        biblioteca_model.registrar_usuario(rut, nombre)
        flash('Usuario registrado exitosamente')
        return redirect(url_for('index'))

@app.route('/prestar_libro/<int:libro_id>/<string:rut_usuario>')
def prestar_libro(libro_id, rut_usuario):
    result = biblioteca_model.prestar_libro(libro_id, rut_usuario)
    if result:
        flash('Libro prestado exitosamente')
    else:
        flash('El libro no está disponible')
    return redirect(url_for('index'))

@app.route('/devolver_libro/<int:libro_id>/<string:rut_usuario>')
def devolver_libro(libro_id, rut_usuario):
    result = biblioteca_model.devolver_libro(libro_id, rut_usuario)
    if result:
        flash('Libro devuelto exitosamente')
    else:
        flash('No se pudo devolver el libro')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
