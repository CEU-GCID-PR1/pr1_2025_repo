from parametros import RADIAN_TO_DEGREE

# Definimos las funciones básicas de la calculadora

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return a ** 0.5

# Función creativa: valor absoluto
def valor_absoluto(a):
    return abs(a)

# Función creativa: módulo (resto de la división)
def modulo(a, b):
    if b == 0:
        return "Error: No se puede calcular el módulo con divisor cero"
    return a % b

# Función para convertir radianes a grados
def radianes_a_grados(radianes):
    return radianes * RADIAN_TO_DEGREE

# Bloque de pruebas si el archivo se ejecuta directamente
if __name__ == "__main__":
    # Pruebas de las funciones básicas
    print(f"Suma de 3 y 5: {suma(3, 5)}")
    print(f"Resta de 10 y 7: {resta(10, 7)}")
    print(f"Multiplicación de 4 y 6: {multiplicacion(4, 6)}")
    print(f"División de 8 entre 2: {division(8, 2)}")
    print(f"Potencia de 2 elevado a 3: {potencia(2, 3)}")
    print(f"Raíz cuadrada de 16: {raiz_cuadrada(16)}")

    # Pruebas de las funciones creativas
    print(f"Valor absoluto de -5: {valor_absoluto(-5)}")
    print(f"Módulo de 10 entre 3: {modulo(10, 3)}")

    # Prueba de divisiones y raíces con errores
    print(f"División de 5 entre 0: {division(5, 0)}")
    print(f"Raíz cuadrada de -9: {raiz_cuadrada(-9)}")
