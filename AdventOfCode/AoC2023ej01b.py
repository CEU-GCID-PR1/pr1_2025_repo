texto = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

numerosTexto = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lineas = texto.split()
suma = 0

def compruebaNumerosTexto(linea, sentido):# asdasdothree
    if (sentido == 1):
        for i,num in enumerate(numerosTexto):
            if num == linea[:len(num)]:
                return i + 1
    else:
        i = 0
        while i < len(numerosTexto):
            num = numerosTexto[i]
            if num == linea[-len(num):]:
                return i + 1
            i += 1
    return -1

for linea in lineas: #zoneight234
    primerDigito = ""
    ultimoDigito = ""
    i = 0
    for caracter in linea:
        if (caracter.isdigit()):
            primerDigito = caracter
            break
        else:
            numero = compruebaNumerosTexto(linea[i:], 1)
            if numero >= 0:
                primerDigito = str(numero)
                break
        i += 1
    i = len(linea)
    for caracter in reversed(linea): # eightwothreee
        if (caracter.isdigit()):
            ultimoDigito = caracter
            break
        else:
            numero = compruebaNumerosTexto(linea[:i], -1)
            if numero >= 0:
                ultimoDigito = str(numero)
                break
        i -= 1
    suma += int(primerDigito + ultimoDigito)

print (suma)