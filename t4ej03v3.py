import csv
import datetime

alumnos = []

with open('alumnos.csv', encoding='UTF-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for alumno in csv_reader:
        alumnos.append(alumno)
        respuesta = ""
        fecha = str(datetime.date.today())
        while respuesta not in ["s","n"]:
            respuesta = input(f"Asistencia de {alumno["nombre"]} (s/n): ").lower()
        if respuesta == "s":
            alumno[fecha] = 1
        else:
            alumno[fecha] = 0

with open('alumnos.csv', mode='w', newline='', encoding='UTF-8') as csv_file:
    cabeceras = alumnos[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=cabeceras) 
    writer.writeheader()
    writer.writerows(alumnos)
