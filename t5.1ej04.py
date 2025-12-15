# Escribe un programa que cargue el archivo “adultos.csv” en un array. Ten en cuenta que tiene una 
# cabecera indicando el significado de cada una. Usando lo que hemos visto en clase calcula en este 
# programa:  
# 1. el porcentaje de mujeres que tienen un ingreso superior a 50k anual. 
# 2. el porcentaje de hombres que tienen ingreso superior a 50k anual. 
# 3. el porcentaje de personas blancas que tienen un ingreso superior a 50k anual. 
# 4. el porcentaje de personas negras que tienen ingreso superior a 50k anual sobre el total. 
# 5. el porcentaje de personas asiáticas que tienen ingreso superior a 50k anual. 
# 6. el porcentaje de personas de otras razas que tienen ingreso superior a 50k anual. 
# 7. el porcentaje de personas menores de 30 años que tienen ingreso superior a 50k anual. 
# 8. el porcentaje de personas entre 30 y 55 años que tienen ingreso superior a 50k anual. 
# 
# 
# 9. el porcentaje de personas mayores de 55 años que tienen ingreso superior a 50k anual. 
# 10. el porcentaje de personas con una educación igual o superior a 10 (educación universitaria) 
# que tienen un ingreso superior a 50k anual.
import numpy as np
import sys
import os

columnas = list(np.loadtxt(os.path.join(sys.path[0], 'adultos.csv'), delimiter=";", max_rows=1, dtype=str))
datos = np.loadtxt(os.path.join(sys.path[0], 'adultos.csv'), delimiter=";", skiprows=1)

edad_column = columnas.index("age")
nivel_edu_column = columnas.index("education.num")
raza_column = columnas.index("race")
sexo_column = columnas.index("sex")
ganancias_columns = columnas.index("income")

# el porcentaje de mujeres que tienen un ingreso superior a 50k anual.
mujeres = datos[datos[:, sexo_column] == 1]
mujeres_ganancias_alto = mujeres[mujeres[:, ganancias_columns] == 1]
print("El porcentaje de mujeres con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(mujeres_ganancias_alto.shape[0]/mujeres.shape[0]))

# el porcentaje de hombres que tienen ingreso superior a 50k anual.
hombres = datos[datos[:, sexo_column] == 0]
hombres_ganancias_alto = hombres[hombres[:, ganancias_columns] == 1]
print("El porcentaje de hombres con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(hombres_ganancias_alto.shape[0]/hombres.shape[0]))

# el porcentaje de personas blancas que tienen un ingreso superior a 50k anual.
personas_blancas = datos[datos[:, raza_column] == 0]
personas_blancas_ganancias_alto = personas_blancas[personas_blancas[:, ganancias_columns] == 1]
print("El porcentaje de personas blancas con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_blancas_ganancias_alto.shape[0]/personas_blancas.shape[0]))

# el porcentaje de personas negras que tienen ingreso superior a 50k anual sobre el total.
personas_negras = datos[datos[:, raza_column] == 1]
personas_negras_ganancias_alto = personas_negras[personas_negras[:, ganancias_columns] == 1]
print("El porcentaje de personas negras con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_negras_ganancias_alto.shape[0]/personas_negras.shape[0]))

# el porcentaje de personas asiáticas que tienen ingreso superior a 50k anual.
personas_asiaticas = datos[datos[:, raza_column] == 2]
personas_asiaticas_ganancias_alto = personas_asiaticas[personas_asiaticas[:, ganancias_columns] == 1]
print("El porcentaje de personas asiaticas con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_asiaticas_ganancias_alto.shape[0]/personas_asiaticas.shape[0]))

# el porcentaje de personas de otras razas que tienen ingreso superior a 50k anual.
personas_otras_razas = datos[datos[:, raza_column] == 3]
personas_otras_razas_ganancias_alto = personas_otras_razas[personas_otras_razas[:, ganancias_columns] == 1]
print("El porcentaje de personas otras razas con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_otras_razas_ganancias_alto.shape[0]/personas_otras_razas.shape[0]))

# el porcentaje de personas menores de 30 años que tienen ingreso superior a 50k anual.
personas_me_30 = datos[datos[:, edad_column] < 30]
personas_me_30_ganancias_alto = personas_me_30[personas_me_30[:, ganancias_columns] == 1]
print("El porcentaje de personas menores de 30 años con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_me_30_ganancias_alto.shape[0]/personas_me_30.shape[0]))

# el porcentaje de personas entre 30 y 55 años que tienen ingreso superior a 50k anual.
personas_30_55 = datos[np.logical_and(30 <= datos[:, edad_column], datos[:, edad_column] <= 55)]
#personas_30_55 = datos[(30 <= datos[:, edad_column]) & (datos[:, edad_column] <= 55)]
personas_30_55_ganancias_alto = personas_30_55[personas_30_55[:, ganancias_columns] == 1]
print("El porcentaje de personas mayores de 30 y menores de 55 años con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_30_55_ganancias_alto.shape[0]/personas_30_55.shape[0]))

# el porcentaje de personas mayores de 55 años que tienen ingreso superior a 50k anual.
personas_ma_55 = datos[datos[:, edad_column] > 55]
personas_ma_55_ganancias_alto = personas_ma_55[personas_ma_55[:, ganancias_columns] == 1]
print("El porcentaje de personas mayores de 55 años con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_ma_55_ganancias_alto.shape[0]/personas_ma_55.shape[0]))

# el porcentaje de personas con una educación igual o superior a 10 (educación universitaria) que tienen un ingreso superior a 50k anual.
personas_ed_10 = datos[datos[:, nivel_edu_column] >= 10]
personas_ed_10_ganancias_alto = personas_ed_10[personas_ed_10[:, ganancias_columns] == 1]
print("El porcentaje de personas con educación universitaria con ingresos mayores de 50k anual es: ",
      '{:2.2%}'.format(personas_ed_10_ganancias_alto.shape[0]/personas_ed_10.shape[0]))