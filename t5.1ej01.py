# Implementa una función llamada elementos_mayores que tome una matriz de NumPy y un 
# número n como argumentos. La función debe devolver una nueva matriz que contenga únicamente los 
# elementos que son mayores que n. Úsala con un array con varios números.
import numpy as np
def elementos_mayores (matriz, n):
    return matriz[matriz > n]

M = np.arange(8).reshape(2,4)
print(elementos_mayores(M, 4))
