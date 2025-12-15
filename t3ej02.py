import random
numero_secreto = random.randrange(1,101)
numero_elegido = 0
intentos = 0
correcto = False
while not correcto:
    numero_elegido = int(input("Indroduzca un número entre el 1 y el 100: "))
    if numero_elegido >= 1 and numero_elegido <= 100:
        intentos += 1
        if numero_elegido == numero_secreto:
            print("¡Enhorabuena!")
            print("Intentos:",intentos)
            correcto = True
        else:
            print("Numero incorrecto")
            if numero_elegido > numero_secreto:
                print("El numero que buscas es menor")
            else:
                print("El numero que buscas es mayor")
    else:
        print("El número tiene que estar entre el 1 y el 100")
