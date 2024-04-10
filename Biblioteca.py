#Examen Final Programacion II
#Autor: Héctor Alfonzo
#Fecha: 09/04/2024
#Sistema de Biblioteca


class Libro:
    libros_disponibles = []

    def __init__(self, titulo, autor, editorial, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.cantidad = cantidad
        Libro.libros_disponibles.append(self)

    def mostrar(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Editorial:", self.editorial)
        print("Cantidad disponible:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print("Se han ingresado", cantidad, "ejemplares del libro", self.titulo)
        else:
            print("La cantidad ingresada debe ser mayor que 0.")

    def retirar(self, cantidad, usuario):
        if cantidad > 0 and cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print("Se han retirado", cantidad, "ejemplares del libro", self.titulo, "por el usuario", usuario)
        elif cantidad > self.cantidad:
            print("No hay suficientes ejemplares disponibles para retirar.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    @classmethod
    def mostrar_libros_disponibles(cls):
        print("Lista de libros disponibles:")
        for libro in cls.libros_disponibles:
            libro.mostrar()


class Usuario:
    usuarios = []

    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.tipo = self.calcular_tipo()
        Usuario.usuarios.append(self)
        self.historial_prestamos = []

    def calcular_tipo(self):
        if 18 <= self.edad < 30:
            return "estudiante"
        elif self.edad >= 30:
            return "docente"
        else:
            return "desconocido"

    @classmethod
    def mostrar_tipo_usuario(cls, dni):
        for usuario in cls.usuarios:
            if usuario.dni == dni:
                print(f"{usuario.nombre} es {usuario.tipo}")

    @classmethod
    def mostrar_usuarios(cls):
        print("Lista de usuarios:")
        for usuario in cls.usuarios:
            print(f"Nombre: {usuario.nombre}, DNI: {usuario.dni}, Edad: {usuario.edad}, Tipo: {usuario.tipo}")

    @classmethod
    def agregar_usuario(cls):
        nombre = input("Ingrese el nombre del usuario: ")
        dni = input("Ingrese el DNI del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        cls(nombre, dni, edad)

    def agregar_prestamo(self, prestamo):
        self.historial_prestamos.append(prestamo)

    def mostrar_historial_prestamos(self):
        print("Historial de préstamos para el usuario", self.nombre)
        if not self.historial_prestamos:
            print("El usuario no tiene historial de préstamos.")
        else:
            for prestamo in self.historial_prestamos:
                print("Libro:", prestamo.libro.titulo)
                print("Fecha de inicio:", prestamo.fecha_inicio)
                print("Fecha de fin:", prestamo.fecha_fin)
                print()


class Prestamo:
    prestamos = []

    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_inicio = None
        self.fecha_fin = None
        Prestamo.prestamos.append(self)
        usuario.agregar_prestamo(self)

    def realizar_prestamo(self):
        if self.libro.cantidad > 0:
            self.libro.cantidad -= 1
            print("Préstamo realizado con éxito para el libro", self.libro.titulo, "a", self.usuario.nombre)
        else:
            print("No hay ejemplares disponibles para prestar.")

    def devolver_prestamo(self):
        self.libro.cantidad += 1
        print("Devolución realizada con éxito para el libro", self.libro.titulo, "de", self.usuario.nombre)


class EsEstudiante:
    @staticmethod
    def validar(edad):
        if 18 <= edad < 30:
            return True
        else:
            return False


def mostrar_menu():
    print("\nBienvenido al sistema de biblioteca de la UCOM")
    print("1. Mostrar información de un libro - mostrar()")
    print("2. Ingresar ejemplares de un libro - ingresar(cantidad)")
    print("3. Retirar ejemplares de un libro - retirar(cantidad, usuario)")
    print("4. Mostrar lista de libros disponibles - mostrar_libros_disponibles()")
    print("5. Mostrar lista de usuarios - mostrar_usuarios()")
    print("6. Verificar si un usuario es estudiante o docente - es_estudiante()")
    print("7. Agregar usuario - agregar_usuario()")
    print("8. Realizar un préstamo - realizar_prestamo()")
    print("9. Devolver un préstamo - devolver_prestamo()")
    print("10. Mostrar lista de libros")
    print("11. Ver historial de préstamos de un usuario - mostrar_historial_prestamos()")
    print("0. Salir")


def main():
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "DeBolsillo", 3)
    libro2 = Libro("Padre Rico, Padre Pobre", "Hector Alfonzo", "DeBolsillo", 2)
    libro3 = Libro("El nombre del viento", "Patrick Rothfuss", "DeBolsillo", 1)
    libro4 = Libro("Cien años de soledad", "Gabriel García Márquez", "Diana", 8)

    # Agregar al menos un usuario
    usuario1 = Usuario("Hector Alfonzo", "3642989", 25)
    usuario2 = Usuario("Jose Roberto", "1234567", 32)
    usuario3 = Usuario("Emilo Britez", "123", 38)
    usuario4 = Usuario("Hugo Lugo", "12345678", 20)

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            Libro.mostrar_libros_disponibles()
        elif opcion == "2":
            cantidad = int(input("Ingrese la cantidad de ejemplares a ingresar: "))
            libro = int(input("Ingrese el número de libro al que desea ingresar ejemplares (1 o 2): "))
            if libro == 1:
                libro1.ingresar(cantidad)
            elif libro == 2:
                libro2.ingresar(cantidad)
            else:
                print("Número de libro inválido.")
        elif opcion == "3":
            cantidad = int(input("Ingrese la cantidad de ejemplares a retirar: "))
            usuario = input("Ingrese el DNI del usuario que retira el libro: ")
            libro = int(input("Ingrese el número de libro que desea retirar (1 o 2): "))
            if libro == 1:
                libro1.retirar(cantidad, usuario)
            elif libro == 2:
                libro2.retirar(cantidad, usuario)
            else:
                print("Número de libro inválido.")
        elif opcion == "4":
            Libro.mostrar_libros_disponibles()
        elif opcion == "5":
            Usuario.mostrar_usuarios()
        elif opcion == "6":
            dni = input("Ingrese el DNI del usuario: ")
            usuario = next((u for u in Usuario.usuarios if u.dni == dni), None)
            if usuario:
                if EsEstudiante.validar(usuario.edad):
                    print(f"{usuario.nombre} es estudiante.")
                else:
                    print(f"{usuario.nombre} no es estudiante.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "7":
            Usuario.agregar_usuario()
        elif opcion == "8":
            dni = input("Ingrese el DNI del usuario que realizará el préstamo: ")
            nombre = input("Ingrese el nombre del usuario: ")
            edad = int(input("Ingrese la edad del usuario: "))
            usuario = Usuario(nombre, dni, edad)
            libro = int(input("Ingrese el número de libro que desea prestar (1 o 2): "))
            if libro == 1:
                prestamo = Prestamo(libro1, usuario)
            elif libro == 2:
                prestamo = Prestamo(libro2, usuario)
            else:
                print("Número de libro inválido.")
            prestamo.realizar_prestamo()
        elif opcion == "9":
            dni = input("Ingrese el DNI del usuario que devolverá el préstamo: ")
            usuario = Usuario(dni)
            libro = int(input("Ingrese el número de libro que desea devolver (1 o 2): "))
            for prestamo in Prestamo.prestamos:
                if prestamo.libro == libro1 and prestamo.usuario.dni == usuario.dni:
                    prestamo.devolver_prestamo()
                    Prestamo.prestamos.remove(prestamo)
                    break
                elif prestamo.libro == libro2 and prestamo.usuario.dni == usuario.dni:
                    prestamo.devolver_prestamo()
                    Prestamo.prestamos.remove(prestamo)
                    break
            else:
                print("El usuario no tiene préstamos pendientes para ese libro.")
        elif opcion == "10":
            Libro.mostrar_libros_disponibles()
        elif opcion == "11":
            dni = input("Ingrese el DNI del usuario para ver su historial de préstamos: ")
            for usuario in Usuario.usuarios:
                if usuario.dni == dni:
                    usuario.mostrar_historial_prestamos()
                    break
            else:
                print("Usuario no encontrado.")
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()
