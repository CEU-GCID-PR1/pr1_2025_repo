# Escribe una función llamada normalizar que reciba una matriz de NumPy y un modo que es una 
# cadena de texto. Y normalice la matriz dependiendo del modo de las siguientes maneras: 
# Para normalizar se suma el valor absoluto mayor de los elementos negativos y luego se divide por el 
# elemento mayor. 
# • Por_defecto: normaliza en general sobre toda la matriz. Si no se ha indicado ningún modo, 
# esta es la opción por defecto. 
# • Columnas: normaliza cada columna por separado. 
# • Filas: normaliza cada fila por separado. 
# • Centrada_en_cero: Una vez normalizada se resta 0.5 a todos los valores para que el rango 
# vaya de -0.5 a 0.5 con centro en cero.
import numpy as np

def normalizar(matriz, modo="Por_defecto"):
    matriz_norm = None
    match modo:
        case "Por_defecto":
            # minimo = np.min(matriz)
            # if minimo < 0:
            #    matriz = matriz + abs(minimo)
            matriz_norm = norm_por_defecto(matriz)
        case "Columnas":
            minimo = matriz.min(axis=0)
            min_neg = np.where(minimo < 0, abs(minimo), 0)
            matriz += min_neg
            matriz_norm = matriz / matriz.max(axis=0)
        case "Filas":
            minimo = matriz.min(axis=1)
            min_neg = np.where(minimo < 0, abs(minimo), 0)
            min_neg_col = min_neg.reshape(-1,1)
            matriz += min_neg_col
            max = matriz.max(axis=1)
            max_col = max.reshape(-1,1)
            matriz_norm = matriz / max_col
        case "Centrada_en_cero":
            matriz_norm = norm_por_defecto(matriz) - 0.5
        case _:
            raise ValueError("El modo no es correcto")
    return matriz_norm

def norm_por_defecto(matriz):
    if matriz[matriz < 0].any():
        matriz -= np.min(matriz)
    return matriz / np.max(matriz)

M = np.array([[1,-2,4,3],[2,-1,3,6],[-1,5,3,-2]])
print(M)
print(normalizar(M))

print(normalizar(M, "Columnas"))
print(normalizar(M, "Filas"))
print(normalizar(M, "Centrada_en_cero"))
print(normalizar(M, "Otro"))
