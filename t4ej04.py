def procesar_fichero(nombre_fichero):
    letras = {}
    with open(nombre_fichero, 'r', encoding='UTF-8') as reader:
        texto = reader.read()
        for caracter in texto:
            if caracter in letras:
                letras[caracter] += 1
            else:
                letras[caracter] = 1
    return letras

print(procesar_fichero("el_quijote.txt"))