import csv
import datetime

lista_nombres = []
asistencia = {}
with open('alumnos.csv', encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    next(csv_reader)
    for fila in csv_reader:
        # lista_nombres.append(fila[0])
        nombre = fila[0]
        respuesta = ""
        while respuesta not in ["s","n"]:
            respuesta = input(f"Asistencia de {nombre} (s/n): ").lower()
        if respuesta == "s":
            asistencia[nombre] = 1
        else:
            asistencia[nombre] = 0

with open('alumnos.csv', mode='w', newline='', encoding='UTF-8') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['nombre', datetime.date.today()]) 
    header = f"nombre,{datetime.date.today()}\n"
    for key in asistencia:
        csv_writer.writerow([key, asistencia[key]]) 
