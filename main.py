import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    print("\n=== CALCULADORA ===")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Sumar N números")
    print("6. Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", sumar.sumar(a, b))

    elif opcion == "2":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", resta.restar(a, b))

    elif opcion == "3":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", multiplicacion.multiplicar(a, b))

    elif opcion == "4":
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Resultado:", dividir.dividir(a, b))

    elif opcion == "5":
        numeros = input("Escribe los números separados por espacio: ").split()
        numeros = [float(n) for n in numeros]
        print("Resultado:", suma_avanzada.suma_avanzada(numeros))

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta otra vez.")
