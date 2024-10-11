class BibliotecaView:
    def mostrar_menu(self):
        print("\n--- Menú Biblioteca ---")
        print("1. Ver catálogo de libros")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")

    def mostrar_libros(self, libros):
        print("\nCatálogo de libros:")
        for libro in libros:
            print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, ISBN: {libro[3]}, Disponible: {'Sí' if libro[4] else 'No'}")

    def solicitar_rut(self):
        return input("Introduce el RUT del usuario: ")

    def solicitar_nombre(self):
        return input("Introduce el nombre del usuario: ")

    def solicitar_libro_id(self):
        return int(input("Introduce el ID del libro: "))

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
