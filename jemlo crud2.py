import csv

class TablaUsuarios:
    def __init__(self):
        self.usuarios = []
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open('usuarios.csv', 'r', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                for fila in lector_csv:
                    self.usuarios.append({'nombre': fila[0], 'identificacion': fila[1]})
        except FileNotFoundError:
            pass

    def guardar_datos(self):
        with open('usuarios.csv', 'w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            for usuario in self.usuarios:
                escritor_csv.writerow([usuario['nombre'], usuario['identificacion']])

    def agregar_usuario(self, nombre, identificacion):
        self.usuarios.append({'nombre': nombre, 'identificacion': identificacion})
        self.guardar_datos()

    def mostrar_usuarios(self):
        for i, usuario in enumerate(self.usuarios):
            print(f"{i + 1}. Nombre: {usuario['nombre']}, Identificación: {usuario['identificacion']}")

    def modificar_usuario(self, indice, nombre, identificacion):
        if 0 <= indice < len(self.usuarios):
            self.usuarios[indice] = {'nombre': nombre, 'identificacion': identificacion}
            self.guardar_datos()
        else:
            print("Índice de usuario no válido.")

    def eliminar_usuario(self, indice):
        if 0 <= indice < len(self.usuarios):
            del self.usuarios[indice]
            self.guardar_datos()
        else:
            print("Índice de usuario no válido.")

tabla = TablaUsuarios()

while True:
    print("\n1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del usuario: ")
        identificacion = input("Ingrese la identificación del usuario: ")
        tabla.agregar_usuario(nombre, identificacion)
    elif opcion == '2':
        tabla.mostrar_usuarios()
    elif opcion == '3':
        indice = int(input("Ingrese el índice del usuario que desea modificar: ")) - 1
        nombre = input("Ingrese el nuevo nombre del usuario: ")
        identificacion = input("Ingrese la nueva identificación del usuario: ")
        tabla.modificar_usuario(indice, nombre, identificacion)
    elif opcion == '4':
        indice = int(input("Ingrese el índice del usuario que desea eliminar: ")) - 1
        tabla.eliminar_usuario(indice)
    elif opcion == '5':
        break
    else:
        print("Opción no válida.")
