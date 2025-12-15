datos = '''199
200
208
210
200
207
240
269
260
263'''

lineas = datos.split()
contador = 0
n0 = int(lineas[0])
n1 = int(lineas[1])
n2 = int(lineas[2])

for i in range(len(lineas) - 3):
    n3 = int(lineas[i+3])
    if n1 + n2 + n3 > n0 + n1 + n2:
        contador += 1
    n0 = n1
    n1 = n2
    n2 = n3

""" for i in range(len(lineas) - 3):
    suma1 = int(lineas[i]) + int(lineas[i+1]) + int(lineas[i+2])
    suma2 = int(lineas[i+1]) + int(lineas[i+2]) + int(lineas[i+3])
    if suma2 > suma1:
        contador += 1 """

print(contador)
