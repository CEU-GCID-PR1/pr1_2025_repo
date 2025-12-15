# Escribe una función llamada normalizar que reciba un dataframe, las columnas y un modo que es 
# una cadena de texto. Normalice la matriz dependiendo del modo de las siguientes maneras: 
# Para normalizar se suma el valor absoluto mayor de los elementos negativos y luego se divide por el 
# elemento mayor. 
# • Por_defecto: normaliza en general sobre toda la matriz. Si no se ha indicado ningún modo, 
# esta es la opción por defecto. 
# • Estandarizar: en vez de normalizar, estandariza de la siguiente manera: resta la media de 
# los valores y divide por la desviación estándar. 
# • Centrada_en_cero: Una vez normalizada se resta 0.5 a todos los valores para que el rango 
# vaya de -0.5 a 0.5 con centro en cero.
import pandas as pd

def normalizar(df, columnas, modo="Por_defecto"):
    dfn = df.copy()
    match modo:
        case "Por_defecto":
            dfn = norm(dfn,columnas)
        case "Centrada_en_cero":
            dfn = norm(dfn,columnas)
            dfn[columnas] -= 0.5
        case "Estandarizar":
            dfn[columnas] = (dfn[columnas] - dfn[columnas].mean() ) / dfn[columnas].std()
    return dfn

def norm(dfn, columnas):
    for col in columnas:
        if (dfn[col]<0).any():
            min = dfn[col].min()
            dfn[col] -= min
        dfn[col] /= dfn[col].max()
    return dfn


dataframe = pd.DataFrame({'c1': [1,2,3],
                          'c2': [3,-4,5],
                          'c3': [7,8,-9]})

print(dataframe)
print(normalizar(dataframe, ['c1','c2'],"Por_defecto"))
print(normalizar(dataframe, ['c1','c2'],"Centrada_en_cero"))
print(normalizar(dataframe, ['c1','c2'],"Estandarizar"))