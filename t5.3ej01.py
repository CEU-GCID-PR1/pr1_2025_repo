import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('adultos.csv', sep=';')
data.replace({'sex':{0:'Hombre', 1:'Mujer'},
                   'race':{0:'Blanca',1:'Negra',2:'Asiatica',3:'Otros'},
                   'income':{-1: '<=50k', 1: '>50k'}}, inplace=True)

# Genera y muestra un gráfico de barras que muestre el número de mujeres y hombres en función de los 
# ingresos que tenga. Como se muestra en la siguiente figura.

data.groupby(["sex", "income"]).size().unstack().plot(
    kind="bar",
    title="Número de mujeres y hombres con altas y bajas ganancias",
    figsize=[6,3]
)
plt.xticks(rotation="horizontal")
plt.show()
plt.close()