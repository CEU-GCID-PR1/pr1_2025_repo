data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def procesarFichero(nombreFichero):
    with open(nombreFichero, 'r', encoding="UTF-8") as reader:
        return reader.read()

numInvalidIDs = 0
ranges = data.split(",")

for rango in ranges:
    separacion = rango.split("-")
    n1 = int(separacion[0])
    n2 = int(separacion[1])
    while n1 <= n2:
        numStr = str(n1)
        if len(numStr) % 2 == 0:
            nIzq = numStr[0:len(numStr) // 2]
            nDer = numStr[len(numStr) // 2:]
            if nIzq == nDer:
                numInvalidIDs += n1
        n1 += 1
print(numInvalidIDs)
