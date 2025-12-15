# Implementa una función llamada elementos_mayores que tome un dataframe, la etiqueta de una 
# columna y un número n como argumentos. La función debe devolver un nuevo dataframe que 
# contenga sólo las filas que en esa columna son mayores que n.
import pandas as pd

def elementos_mayores(df, col, num):
    dfn = df.copy()
    return dfn[dfn[col] > num]

dataframe = pd.DataFrame({'var1': [1, 2, 3], 'var2': ['uno', 'dos', 'tres'], 'var3': [5,6,9]})
print(dataframe)
print(elementos_mayores(dataframe,'var3',5))
