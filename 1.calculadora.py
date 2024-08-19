def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def mostrar_menu():
    print("\n--- Calculadora Básica ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = input("Elija una operación (1-5): ")
            
            if opcion == '5':
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break
            
            if opcion not in ['1', '2', '3', '4']:
                print("Opción no válida. Por favor, elija una opción del 1 al 5.")
                continue
            
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                resultado = suma(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = resta(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcion == '4':
                resultado = division(num1, num2)
                print(f"Resultado: {num1} / {num2} = {resultado}")
                
        except ValueError:
            print("Error: Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()