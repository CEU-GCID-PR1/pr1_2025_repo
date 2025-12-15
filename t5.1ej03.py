# Escribe una función llamada estandarizar que reciba una matriz de NumPy y un modo que es una 
# cadena de texto. Estandarice la matriz dependiendo del modo según lo siguiente: 
# Para estandarizar se debe restar la media de los valores y dividir por la desviación estándar. 
# • Por_defecto: estandariza en general sobre toda la matriz. 
# • Columnas: estandariza cada columna por separado. 
# • Filas: estandariza cada fila por separado. 

import numpy as np

def estandarizar(matriz, modo="defecto"):
    matriz_n = matriz.copy()
    filas, _ = matriz_n.shape

    # Mejora, compruebo que el primer argumento es un array
    if type(matriz) != np.ndarray:
        raise ValueError("El primer argumento de la función debe ser un array.")
    
    if modo=="defecto":
        mean = matriz_n.mean()
        std = matriz_n.std()
        matriz_n = (matriz_n - mean)/std
    elif modo=="columnas":
        mean = matriz_n.mean(axis=0)
        std = matriz_n.std(axis=0)
        matriz_n = (matriz_n - mean)/std
    elif modo=="filas":
        mean = matriz_n.mean(axis=1).reshape(filas,1)
        std = matriz_n.std(axis=1).reshape(filas,1)
        matriz_n = (matriz_n - mean)/std
    else:
        raise ValueError("El modo introducido no es correcto.")

    return matriz_n

matriz = np.array([[1,2,3,4],
                   [4,5,6,7],
                   [7,8,9,10]],
                   dtype=float)

print("La matriz original es:")
print(matriz)
print("La matriz estandarizada:")
print(estandarizar(matriz))
print("La matriz estandarizada por columnas:")
print(estandarizar(matriz, modo="columnas"))
print("La matriz estandarizada por filas:")
print(estandarizar(matriz, modo="filas"))
