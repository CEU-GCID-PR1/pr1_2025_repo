texto = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

lineas = texto.split()
suma = 0

for linea in lineas:
    primerDigito = ""
    ultimoDigito = ""
    for caracter in linea:
        if (caracter.isdigit()):
            primerDigito = caracter
            break;
    for caracter in reversed(linea):
        if (caracter.isdigit()):
            ultimoDigito = caracter
            break;
    suma += int(primerDigito + ultimoDigito)

print (suma)
