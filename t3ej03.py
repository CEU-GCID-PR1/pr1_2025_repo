def calculadora(operacion):
    resultado = 0
    check = True
    i = 0
    while (check):
        print("Iteracion", i)
        if (operacion[i] == "+"):
            x, y = getNumeros(operacion, i)
            resultado =  x + y
            check = False
        elif (operacion[i] == "-"):
            x, y = getNumeros(operacion, i)
            resultado =  x - y
            check = False
        elif (operacion[i] == "*"):
            x, y = getNumeros(operacion, i)
            resultado =  x * y
            check = False
        elif (operacion[i] == "/"):
            x, y = getNumeros(operacion, i)
            resultado =  x / y
            check = False
        i += 1
    return resultado

def getNumeros(operacion, i):
    return int(operacion[0:i]), int(operacion[i+1:])

print(calculadora("12354*1234123434")) # + - * /
print(eval("12354*12341"))