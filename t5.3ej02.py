import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('adultos.csv', sep=';')
data.replace({'sex':{0:'Hombre', 1:'Mujer'},
                   'race':{0:'Blanca',1:'Negra',2:'Asiatica',3:'Otros'},
                   'income':{-1: '<=50k', 1: '>50k'}}, inplace=True)

# Genera una única figura con dos gráficas de barras en las cuales se muestre el número de mujeres en 
# uno y el de hombres en otro, en función del número de ingresos y la educación. Como se muestra en 
# la siguiente figura.

fig, axes = plt.subplots(nrows=2, ncols=1)
data[data['sex'] == 'Mujer'].groupby(['education.num', 'income']).size().unstack().plot(
    ax=axes[0],
    kind='bar',
    title='Ingresos de mujeres por educación'
)
data[data['sex'] == 'Hombre'].groupby(['education.num', 'income']).size().unstack().plot(
    ax=axes[1],
    kind='bar',
    title='Ingresos de hombres por educación'
)

plt.xticks(rotation="horizontal")
fig.tight_layout()
plt.show()
plt.close()
