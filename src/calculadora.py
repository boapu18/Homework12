import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def exponenciacion(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(a)

def menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponenciación")
    print("6. Raíz Cuadrada")
    print("7. Salir")

    return int(input("Ingrese el número de la operación: "))

def main():
    while True:
        opcion = menu()
        if opcion == 7:
            break
        elif opcion == 6:
            a = float(input("Ingrese el número: "))
            print(f"Raíz Cuadrada de {a} = {raiz_cuadrada(a)}")
        else:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            if opcion == 1:
                print(f"{a} + {b} = {suma(a, b)}")
            elif opcion == 2:
                print(f"{a} - {b} = {resta(a, b)}")
            elif opcion == 3:
                print(f"{a} * {b} = {multiplicacion(a, b)}")
            elif opcion == 4:
                try:
                    print(f"{a} / {b} = {division(a, b)}")
                except ValueError as e:
                    print(e)
            elif opcion == 5:
                print(f"{a} ^ {b} = {exponenciacion(a, b)}")
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

