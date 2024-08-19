class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self):
        try:
            name = input("Ingrese el nombre del producto: ")
            quantity = int(input("Ingrese la cantidad: "))
            price = float(input("Ingrese el precio: "))
            self.products.append(Product(name, quantity, price))
            print("Producto agregado con éxito.")
        except ValueError:
            print("Error: Ingrese datos válidos.")

    def show_products(self):
        if not self.products:
            print("El inventario está vacío.")
        else:
            for product in self.products:
                print(f"Nombre: {product.name}, Cantidad: {product.quantity}, Precio: ${product.price:.2f}")

    def search_product(self):
        name = input("Ingrese el nombre del producto a buscar: ")
        for product in self.products:
            if product.name.lower() == name.lower():
                print(f"Nombre: {product.name}, Cantidad: {product.quantity}, Precio: ${product.price:.2f}")
                return
        print("Producto no encontrado.")

    def update_quantity(self):
        name = input("Ingrese el nombre del producto a actualizar: ")
        for product in self.products:
            if product.name.lower() == name.lower():
                try:
                    new_quantity = int(input("Ingrese la nueva cantidad: "))
                    product.quantity = new_quantity
                    print("Cantidad actualizada con éxito.")
                    return
                except ValueError:
                    print("Error: Ingrese una cantidad válida.")
                    return
        print("Producto no encontrado.")

    def remove_product(self):
        name = input("Ingrese el nombre del producto a eliminar: ")
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print("Producto eliminado con éxito.")
                return
        print("Producto no encontrado.")

def main():
    inventory = Inventory()
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")
        
        try:
            choice = int(input("Seleccione una opción: "))
            if choice == 1:
                inventory.add_product()
            elif choice == 2:
                inventory.show_products()
            elif choice == 3:
                inventory.search_product()
            elif choice == 4:
                inventory.update_quantity()
            elif choice == 5:
                inventory.remove_product()
            elif choice == 6:
                print("Gracias por usar el sistema de inventario. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()