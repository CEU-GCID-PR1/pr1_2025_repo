# Archivo principal: main.py

# Importamos las funciones desde el archivo funciones.py
from funciones import *

def mostrar_menu():
    print("\nCalculadora")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Radianes a grados")
    print("8. Salir")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Introduce el número de la operación que deseas realizar: ")

        if opcion == '8':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4', '5']:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        
        if opcion == '1':
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == '4':
            print(f"Resultado: {division(num1, num2)}")
        elif opcion == '5':
            print(f"Resultado: {potencia(num1, num2)}")
        elif opcion == '6':
            num = float(input("Introduce el número: "))
            print(f"Resultado: {raiz_cuadrada(num)}")
        elif opcion == '7':
            num = float(input("Introduce los radianes: "))
            print(f"Resultado: {radianes_a_grados(num)}")
        else:
            print("Opción no válida, por favor elige una opción del menú.")
        
# Ejecución del programa
if __name__ == "__main__":
    ejecutar_calculadora()
