datos = '''1721
979
366
299
675
1456'''

numeros = []
for numero in datos.split():
    numeros.append(int(numero))

contador = 0
procesando = True
while procesando:
    print("\nProcesando: ", numeros[contador])
    for i in range(contador + 1, len(numeros)):
        suma = numeros[contador] + numeros[i]
        print(numeros[contador], " + ", numeros[i], ": ", suma)
        if (suma == 2020):
            print(numeros[contador] * numeros[i])
            procesando = False
    contador += 1
    if (contador == len(numeros) - 1):
        procesando = False
