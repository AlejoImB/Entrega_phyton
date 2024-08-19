class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "Pendiente"

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        try:
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            nueva_tarea = Tarea(titulo, descripcion)
            self.tareas.append(nueva_tarea)
            print("Tarea agregada con éxito.")
        except Exception as e:
            print(f"Error al agregar la tarea: {str(e)}")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. Título: {tarea.titulo}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")

    def buscar_tarea(self):
        titulo = input("Ingrese el título de la tarea a buscar: ")
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(f"Tarea encontrada - Título: {tarea.titulo}, Descripción: {tarea.descripcion}, Estado: {tarea.estado}")
                return
        print("Tarea no encontrada.")

    def actualizar_estado(self):
        titulo = input("Ingrese el título de la tarea a actualizar: ")
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                tarea.estado = "Completada"
                print("Estado de la tarea actualizado a 'Completada'.")
                return
        print("Tarea no encontrada.")

    def eliminar_tarea(self):
        titulo = input("Ingrese el título de la tarea a eliminar: ")
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                self.tareas.remove(tarea)
                print("Tarea eliminada con éxito.")
                return
        print("Tarea no encontrada.")

def mostrar_menu():
    print("\n--- Sistema de Gestión de Tareas ---")
    print("1. Agregar nueva tarea")
    print("2. Mostrar todas las tareas")
    print("3. Buscar tarea por título")
    print("4. Actualizar estado de una tarea")
    print("5. Eliminar tarea")
    print("6. Salir")

def main():
    gestor = GestorTareas()
    while True:
        mostrar_menu()
        try:
            opcion = input("Seleccione una opción (1-6): ")
            if opcion == '1':
                gestor.agregar_tarea()
            elif opcion == '2':
                gestor.mostrar_tareas()
            elif opcion == '3':
                gestor.buscar_tarea()
            elif opcion == '4':
                gestor.actualizar_estado()
            elif opcion == '5':
                gestor.eliminar_tarea()
            elif opcion == '6':
                print("Gracias por usar el Sistema de Gestión de Tareas. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()