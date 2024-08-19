class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class GestorContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        nuevo_contacto = Contacto(nombre, telefono)
        self.contactos.append(nuevo_contacto)
        print("Contacto agregado con éxito.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la lista.")
        else:
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}")

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Contacto encontrado - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}")
                return
        print("Contacto no encontrado.")

    def eliminar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print("Contacto eliminado con éxito.")
                return
        print("Contacto no encontrado.")

def mostrar_menu():
    print("\n--- Gestor de Contactos ---")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def main():
    gestor = GestorContactos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            gestor.agregar_contacto()
        elif opcion == '2':
            gestor.mostrar_contactos()
        elif opcion == '3':
            gestor.buscar_contacto()
        elif opcion == '4':
            gestor.eliminar_contacto()
        elif opcion == '5':
            print("Gracias por usar el Gestor de Contactos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()