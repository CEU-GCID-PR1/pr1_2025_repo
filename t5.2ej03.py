# Escribe un programa que cargue el archivo “adultos.csv” como un dataframe. Ten en cuenta que 
# tiene una cabecera indicando el significado de cada una. Cambia los valores de las columnas “sex” y 
# “race” por los valores correspondientes indicados en la tabla al final.
import pandas as pd

data = pd.read_csv('adultos.csv', sep=';')
data.replace({'sex':{0:'Hombre', 1:'Mujer'},
                   'race':{0:'Blanca',1:'Negra',2:'Asiatica',3:'Otros'},
                   'income':{-1: '<=50k', 1: '>50k'}}, inplace=True)

#1. el porcentaje de mujeres que tienen un ingreso superior a 50k anual.
mujeres = data[(data['sex'] == 'Mujer')]
mujeres_alto_ingreso = data[(data['sex'] == 'Mujer') & (data['income'] == '>50k')]
print('El porcentaje de mujeres que tienen un ingreso superior a 50k anual es: ', len(mujeres_alto_ingreso.index)/len(mujeres.index)*100, '%')

#2. el porcentaje de hombres que tienen ingreso superior a 50k anual.
hombres = data[(data['sex'] == 'Hombre')]
hombres_alto_ingreso = data[(data['sex'] == 'Hombre') & (data['income'] == '>50k')]
print('El porcentaje de hombres que tienen ingreso superior a 50k anual: ', round(len(hombres_alto_ingreso.index)/len(hombres.index)*100, 2), '%')

#3. el porcentaje de personas blancas que tienen un ingreso superior a 50k anual.
raza_blanca = data[(data['race'] == 'Blanca')]
blanca_alto_ingreso = data[(data['race'] == 'Blanca') & (data['income'] == '>50k')]
print('El porcentaje de personas blancas que tienen un ingreso superior a 50k anual: ', round(len(blanca_alto_ingreso.index)/len(raza_blanca.index)*100, 2), '%')

#4. el porcentaje de personas negras que tienen ingreso superior a 50k anual sobre el total.
raza_negra = data[(data['race'] == 'Negra')]
negra_alto_ingreso = data[(data['race'] == 'Negra') & (data['income'] == '>50k')]
print('El porcentaje de personas negras que tienen ingreso superior a 50k anual sobre el total: ', round(len(negra_alto_ingreso.index)/len(raza_negra.index)*100, 2), '%')

#5. el porcentaje de personas asiáticas que tienen ingreso superior a 50k anual.
raza_asiatica = data[(data['race'] == 'Asiatica')]
asiatica_alto_ingreso = data[(data['race'] == 'Asiatica') & (data['income'] == '>50k')]
print('El porcentaje de personas asiáticas que tienen ingreso superior a 50k anual: ', round(len(asiatica_alto_ingreso.index)/len(raza_asiatica.index)*100, 2), '%')

#6. el porcentaje de personas de otras razas que tienen ingreso superior a 50k anual.
raza_otros = data[(data['race'] == 'Otros')]
otros_alto_ingreso = data[(data['race'] == 'Otros') & (data['income'] == '>50k')]
print('El porcentaje de personas de otras razas que tienen ingreso superior a 50k anual: ', round(len(otros_alto_ingreso.index)/len(raza_otros.index)*100, 2), '%')

#7. el porcentaje de personas menores de 30 años que tienen ingreso superior a 50k anual.
m30 = data[(data['age'] < 30)]
m30_alto_ingreso = data[(data['age'] < 30) & (data['income'] == '>50k')]
print('El porcentaje de personas menores de 30 años que tienen ingreso superior a 50k anual: ', round(len(m30_alto_ingreso.index)/len(data.index)*100, 2), '%')

#8. el porcentaje de personas entre 30 y 55 años que tienen ingreso superior a 50k anual.
edad_30_55 = data[(data['age'].between(30, 55))]
edad_30_55_alto_ingreso = data[(data['age'].between(30, 55)) & (data['income'] == '>50k')]
print('El porcentaje de personas entre 30 y 55 años que tienen ingreso superior a 50k anual: ', round(len(edad_30_55_alto_ingreso.index)/len(edad_30_55.index)*100, 2), '%')

#9. el porcentaje de personas mayores de 55 años que tienen ingreso superior a 50k anual.
edad_55 = data[(data['age'] > 55)]
edad_55_alto_ingreso = data[(data['age'] > 55) & (data['income'] == '>50k')]
print('El porcentaje de personas mayores de 55 años que tienen ingreso superior a 50k anua: ', round(len(edad_55_alto_ingreso.index)/len(edad_55.index)*100, 2), '%')

#10. el porcentaje de personas con una educación igual o superior a 10 (educación universitaria) que tienen un ingreso superior a 50k anual.
estudios_universitarios = data[(data['education.num'] >= 10)]
estudios_universitarios_alto_ingreso = data[(data['education.num'] >= 10) & (data['income'] == '>50k')]
print('El porcentaje de personas con una educación igual o superior a 10 (educación universitaria) que tienen un ingreso superior a 50k anual: ', round(len(estudios_universitarios_alto_ingreso.index)/len(estudios_universitarios.index)*100, 2), '%')