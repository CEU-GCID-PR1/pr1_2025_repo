def nota_media(notas):
    return sum(notas) / len(notas)

def mayusculas(name):
    return name.upper()

def resultados(estudiantes):
    print("\nRESULTADOS FINALES")
    print("----------------------------")
    for nombre in sorted(estudiantes):
        media = nota_media(estudiantes[nombre])
        print(mayusculas(nombre), "-> Media:", round(media, 2))
 
# Diccionario para almacenar estudiantes y sus notas
estudiantes = {}

print("Introduce el nombre del estudiante (escribe 'terminar' para finalizar)")
while True:
    nombre = input("Nombre: ")
    if nombre == "terminar":
        break
    notas_texto = input("Introduce las notas separadas por comas: ")

    # Convertimos las notas a float
    notas = []
    for nota in notas_texto.split(","):
        notas.append(float(nota))
    estudiantes[nombre] = notas

# Mostrar resultados
if len(estudiantes) > 0:
    resultados(estudiantes)
else:
    print("No se han introducido estudiantes.")
