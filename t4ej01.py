import random
import os.path
FICHERO_ALUMNOS = "lista_alumnos.txt"
FICHERO_ALUMNOS_PENDIENTES = "lista_alumnos_pendientes.txt"

def procesarInput(nombreFichero):
    if os.path.exists(nombreFichero):
        with open(nombreFichero, 'r', encoding='UTF-8') as reader:
            return reader.read()
    else:
        return ""

def guardarFichero(alumnos):
    with open('lista_alumnos_pendientes.txt', mode='w', newline='', encoding='UTF-8') as new_file:
        new_file.write('\n'.join(str(alumno) for alumno in alumnos))

alumnos = procesarInput(FICHERO_ALUMNOS_PENDIENTES).splitlines()
if len(alumnos) == 0:
    alumnos = procesarInput(FICHERO_ALUMNOS).splitlines()
    random.shuffle(alumnos)
alumno = alumnos.pop()
print(f"### {alumno} ###")
guardarFichero(alumnos)
