datos = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

dialNumber = 50
password = 0

def procesarFichero(nombreFichero):
    with open(nombreFichero, 'r', encoding="UTF-8") as reader:
        return reader.read()

# lineas = datos.splitlines()
lineas = procesarFichero("Aoc2025ej01_input.txt").splitlines()
for linea in lineas:
    num = int(linea[1:])
    if linea[0] == 'R':
        dialNumber = (dialNumber + num) % 100
    else:
        dialNumber = (dialNumber - num) % 100
    if dialNumber == 0:
        password += 1
print(password)
