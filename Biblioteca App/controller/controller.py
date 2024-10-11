class BibliotecaController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def mostrar_menu(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.mostrar_libros()

            elif opcion == "2":
                self.registrar_usuario()

            elif opcion == "3":
                self.prestar_libro()

            elif opcion == "4":
                self.devolver_libro()

            elif opcion == "5":
                print("Saliendo del programa...")
                break

            else:
                self.vista.mostrar_mensaje("Opción no válida.")

    def mostrar_libros(self):
        libros = self.modelo.obtener_libros()
        self.vista.mostrar_libros(libros)

    def registrar_usuario(self):
        rut = self.vista.solicitar_rut()
        nombre = self.vista.solicitar_nombre()
        self.modelo.registrar_usuario(rut, nombre)
        self.vista.mostrar_mensaje(f"Usuario {nombre} registrado exitosamente.")

    def prestar_libro(self):
        libro_id = self.vista.solicitar_libro_id()
        rut_usuario = self.vista.solicitar_rut()
        if self.modelo.prestar_libro(libro_id, rut_usuario):
            self.vista.mostrar_mensaje("El libro ha sido prestado exitosamente.")
        else:
            self.vista.mostrar_mensaje("El libro no está disponible.")

    def devolver_libro(self):
        libro_id = self.vista.solicitar_libro_id()
        rut_usuario = self.vista.solicitar_rut()
        if self.modelo.devolver_libro(libro_id, rut_usuario):
            self.vista.mostrar_mensaje("El libro ha sido devuelto exitosamente.")
        else:
            self.vista.mostrar_mensaje("El usuario no tiene ese libro prestado.")
