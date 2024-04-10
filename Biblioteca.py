#Examen Final Programacion II
#Autor: Héctor Alfonzo
#Fecha: 09/04/2024
#Sistema User Access Ucom Library


#Importamos datetime para obtener datos de la fecha actual
from datetime import datetime, timedelta

# Aqui declaramos la clase Libro
class Libro:
    libros_disponibles = []
    id_libro_actual = 1

    def __init__(self, titulo, autor, editorial, cantidad):
        self.id_libro = Libro.id_libro_actual
        Libro.id_libro_actual += 1
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.cantidad = cantidad
        Libro.libros_disponibles.append(self)

    def mostrar(self):  # requerimiento de examen
        print("ID:", self.id_libro)
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Editorial:", self.editorial)
        print("Cantidad disponible:", self.cantidad)

    def ingresar(self, cantidad): # requerimiento de examen
        if cantidad > 0:
            self.cantidad += cantidad
            print("Se han ingresado", cantidad, "ejemplares del libro", self.titulo)
        else:
            print("La cantidad ingresada debe ser mayor que 0.")
 
    def retirar(self, cantidad, usuario): # requerimiento de examen
        if cantidad > 0 and cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print("Se han retirado", cantidad, "ejemplares del libro", self.titulo, "por el usuario", usuario)
        elif cantidad > self.cantidad:
            print("No hay suficientes ejemplares disponibles para retirar.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    @classmethod
    def mostrar_libros_disponibles(cls): # requerimiento de examen
        print("Lista de libros disponibles:")
        for libro in cls.libros_disponibles:
            libro.mostrar()


# Aqui declaramos una clase Persona
class Persona:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def es_estudiante(self):
        if 18 <= self.edad < 30:
            return True
        else:
            return False


# Aqui se encuentra la clase Usuario
class Usuario(Persona):
    usuarios = []

    def __init__(self, nombre, dni, edad):
        super().__init__(nombre, dni, edad)
        self.tipo = "Estudiante" if self.es_estudiante() else "Docente"
        Usuario.usuarios.append(self)
        self.historial_prestamos = []

    @classmethod
    def mostrar_usuarios(cls): #requerimiento de examen metodo mostrar()
        print("Lista de usuarios:")
        for usuario in cls.usuarios:
            print(f"Nombre: {usuario.nombre}, DNI: {usuario.dni}, Edad: {usuario.edad}")

    @classmethod
    def agregar_usuario(cls):
        nombre = input("Ingrese el nombre del usuario: ")
        dni = input("Ingrese el DNI del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        cls(nombre, dni, edad)


# Aqui se encuentra la clase Prestamo
class Prestamo:
    prestamos = []

    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_inicio = datetime.now()
        self.fecha_fin = self.fecha_inicio + timedelta(days=7)  
        Prestamo.prestamos.append(self)
        usuario.historial_prestamos.append(self)

    def realizar_prestamo(self): 
        if self.libro.cantidad > 0:
            self.libro.cantidad -= 1
            print("Préstamo realizado con éxito para el libro", self.libro.titulo, "a", self.usuario.nombre)
            print("Fecha de inicio:", self.fecha_inicio.strftime("%Y-%m-%d"))
            print("Fecha de fin:", self.fecha_fin.strftime("%Y-%m-%d"))
        else:
            print("No hay ejemplares disponibles para prestar.")

    def devolver_prestamo(self):
        self.libro.cantidad += 1
        print("Devolución realizada con éxito para el libro", self.libro.titulo, "de", self.usuario.nombre)

    @classmethod
    def mostrar_prestamos(cls): #requerimento de examen
        print("Detalles de todos los préstamos:")
        for prestamo in cls.prestamos:
            print("Usuario:", prestamo.usuario.nombre)
            print("Libro:", prestamo.libro.titulo)
            print("Fecha de inicio:", prestamo.fecha_inicio.strftime("%Y-%m-%d"))
            print("Fecha de fin:", prestamo.fecha_fin.strftime("%Y-%m-%d"))
            print()


#Aqui tenemos un menu para el aplicativo 
def mostrar_menu():
    print("\nBienvenido al sistema de biblioteca de la UCOM")
    print("1. Mostrar información de un libro")
    print("2. Ingresar ejemplares de un libro")
    print("3. Retirar ejemplares de un libro")
    print("4. Mostrar lista de libros disponibles")
    print("5. Mostrar lista de usuarios")
    print("6. Verificar si un usuario es estudiante o docente")
    print("7. Realizar un préstamo")
    print("8. Devolver un préstamo")
    print("9. Mostrar historial de préstamos de un usuario")
    print("10. Agregar usuario")
    print("11. Mostrar detalles de todos los préstamos")
    print("0. Salir")


def main():

    # Aqui se incluyen algunos datos de ejemplo para no utilizar una DB.
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "DeBolsillo", 3)
    libro2 = Libro("Padre Rico, Padre Pobre", "Hector Alfonzo", "DeBolsillo", 2)
    libro3 = Libro("El nombre del viento", "Patrick Rothfuss", "DeBolsillo", 1)
    libro4 = Libro("Cien años de soledad", "Gabriel García Márquez", "Diana", 8)

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
            id_libro = int(input("Ingrese el ID del libro al que desea ingresar ejemplares: "))
            libro = next((lib for lib in Libro.libros_disponibles if lib.id_libro == id_libro), None)
            if libro:
                libro.ingresar(cantidad)
            else:
                print("ID de libro inválido.")
        elif opcion == "3":
            cantidad = int(input("Ingrese la cantidad de ejemplares a retirar: "))
            dni_usuario = input("Ingrese el DNI del usuario que retira el libro: ")
            id_libro = int(input("Ingrese el ID del libro que desea retirar: "))
            libro = next((lib for lib in Libro.libros_disponibles if lib.id_libro == id_libro), None)
            usuario = next((u for u in Usuario.usuarios if u.dni == dni_usuario), None)
            if libro and usuario:
                libro.retirar(cantidad, usuario.nombre)
            else:
                print("ID de libro o DNI de usuario inválido.")
        elif opcion == "4":
            Libro.mostrar_libros_disponibles()
        elif opcion == "5":
            Usuario.mostrar_usuarios()
        elif opcion == "6":
            dni = input("Ingrese el DNI del usuario: ")
            usuario = next((u for u in Usuario.usuarios if u.dni == dni), None)
            if usuario:
                print(f"{usuario.nombre} es {usuario.tipo}")
            else:
                print("Usuario no encontrado.")
        elif opcion == "7":
            Usuario.mostrar_usuarios()
            dni_usuario = input("Ingrese el DNI del usuario que realizará el préstamo: ")
            usuario = next((u for u in Usuario.usuarios if u.dni == dni_usuario), None)
            if usuario:
                Libro.mostrar_libros_disponibles()
                id_libro = int(input("Ingrese el ID del libro que desea prestar: "))
                libro = next((lib for lib in Libro.libros_disponibles if lib.id_libro == id_libro), None)
                if libro:
                    prestamo = Prestamo(libro, usuario)
                    prestamo.realizar_prestamo()
                else:
                    print("Libro no encontrado.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "8":
            dni_usuario = input("Ingrese el DNI del usuario que devolverá el préstamo: ")
            usuario = next((u for u in Usuario.usuarios if u.dni == dni_usuario), None)
            if usuario:
                Prestamo.mostrar_prestamos()
                id_libro = int(input("Ingrese el ID del libro que desea devolver: "))
                prestamo = next((p for p in Prestamo.prestamos if p.libro.id_libro == id_libro and p.usuario.dni == dni_usuario), None)
                if prestamo:
                    prestamo.devolver_prestamo()
                    Prestamo.prestamos.remove(prestamo)
                else:
                    print("No se encontró un préstamo para ese libro o usuario.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "9":
            dni_usuario = input("Ingrese el DNI del usuario para ver su historial de préstamos: ")
            usuario = next((u for u in Usuario.usuarios if u.dni == dni_usuario), None)
            if usuario:
                for prestamo in usuario.historial_prestamos:
                    print("Libro:", prestamo.libro.titulo)
                    print("Fecha de inicio:", prestamo.fecha_inicio.strftime("%Y-%m-%d"))
                    print("Fecha de fin:", prestamo.fecha_fin.strftime("%Y-%m-%d"))
                    print()
            else:
                print("Usuario no encontrado.")
        elif opcion == "10":
            Usuario.agregar_usuario()
        elif opcion == "11":
            Prestamo.mostrar_prestamos()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()

