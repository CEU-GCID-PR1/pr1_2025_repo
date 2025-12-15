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
anterior = 999999

for linea in lineas:
    actual = int(linea)
    if actual > anterior:
        contador += 1
    anterior = actual

print(contador)
