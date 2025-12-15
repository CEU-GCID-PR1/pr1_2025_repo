import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('adultos.csv', sep=';')
data.replace({'sex':{0:'Hombre', 1:'Mujer'},
                   'race':{0:'Blanca',1:'Negra',2:'Asiatica',3:'Otros'},
                   'income':{-1: '<=50k', 1: '>50k'}}, inplace=True)

# Genera una única figura con cuatro gráficas de tipo tarta en las cuales se muestre el número de 
# mujeres en uno y el de hombres en otro, en función del número de ingresos y la educación. Como se 
# muestra en la siguiente figura.

fig, axes = plt.subplots(nrows=2, ncols=2)

datos1 = data[data["sex"] == 'Mujer'].sort_values('education.num')['education.num'].value_counts().sort_index()

wedges, texts, autotexts = axes[0, 0].pie(datos1, autopct='%1.1f%%', pctdistance=1.4)
axes[0,0].set_xlabel("Mujeres por educación.")
anotations = ((datos1/datos1.sum())*100).to_frame().applymap(lambda x: round(x,2))
anotations_list = [str(x[0]) + ' - ' + str(x[1].values[0]) + '%' for x in anotations.iterrows()]
axes[0,0].legend(wedges, anotations_list,
                 title="Nivel de educación",
                 ncol=1,
                 loc="upper right",
                 bbox_to_anchor=(1, 0, 0.5, 1))

for label, pct_label in zip(texts, autotexts):
    label.set_text('')
    pct_label.set_text('')

wedges, texts, autotexts = axes[0, 1].pie(data[data["sex"] == 'Mujer'].income.sort_values().value_counts(), 
                                          autopct='%1.1f%%')
axes[0,1].set_xlabel("Mujeres por ingresos.")
axes[0,1].legend(wedges, data[data["sex"] == 'Mujer'].income.sort_values().value_counts().index,
                 title="Nivel de ingresos",
                 loc="upper left")

datos1 = data[data["sex"] == 'Hombre'].sort_values('education.num')['education.num'].value_counts().sort_index()

wedges, texts, autotexts = axes[1, 0].pie(datos1, autopct='%1.1f%%', pctdistance=0.9, labeldistance=1.1,
                                          radius=1)
axes[1,0].set_xlabel("Hombres por educación.")
anotations = ((datos1/datos1.sum())*100).to_frame().applymap(lambda x: round(x,2))
anotations_list = [str(x[0]) + ' - ' + str(x[1].values[0]) + '%' for x in anotations.iterrows()]
axes[1,0].legend(wedges, anotations_list,
                 title="Nivel de educación",
                 ncol=1,
                 loc="upper right",
                 bbox_to_anchor=(1, 0, 0.5, 1))

for label, pct_label in zip(texts, autotexts):
       label.set_text('')
       pct_label.set_text('')


wedges, texts, autotexts = axes[1, 1].pie(data[data["sex"] == 'Hombre'].income.sort_values().value_counts(), 
                                          autopct='%1.1f%%')
axes[1,1].set_xlabel("Hombres por ingresos.")
axes[1,1].legend(wedges, data[data["sex"] == 'Hombre'].income.sort_values().value_counts().index,
                 title="Nivel de ingresos",
                 loc="upper left")

plt.show()
plt.close()
