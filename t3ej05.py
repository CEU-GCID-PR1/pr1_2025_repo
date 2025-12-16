# Función para añadir un libro a la biblioteca
def añadir_libro(biblioteca, titulo, autor, copias):
    titulo = titulo.upper()
    autor = autor.title()

    if titulo not in biblioteca:
        biblioteca[titulo] = {
            "autor": autor,
            "copias": copias,
            "prestados": 0
        }
    else:
        biblioteca[titulo]["copias"] += copias

# Función para prestar un libro
def prestar_libro(biblioteca, titulo):
    titulo = titulo.upper()

    if titulo in biblioteca:
        disponibles = biblioteca[titulo]["copias"] - biblioteca[titulo]["prestados"]
        if disponibles > 0:
            biblioteca[titulo]["prestados"] += 1
        else:
            print("No hay copias disponibles")
    else:
        print("El libro no existe")

# Función para devolver un libro
def devolver_libro(biblioteca, titulo):
    titulo = titulo.upper()

    if titulo in biblioteca:
        if biblioteca[titulo]["prestados"] > 0:
            biblioteca[titulo]["prestados"] -= 1
        else:
            print("No hay libros prestados de este título")
    else:
        print("El libro no existe")

# Función para listar los libros prestados
def listar_libros(biblioteca):
    print("\nLIBROS PRESTADOS")
    print("--------------------------")
    for titulo in biblioteca:
        if biblioteca[titulo]["prestados"] > 0:
            print("Título:", titulo)
            print("Autor:", biblioteca[titulo]["autor"])
            print("Prestados:", biblioteca[titulo]["prestados"])
            print()

# Diccionario principal de la biblioteca
biblioteca = {}

# Menú principal
while True:
    print("\n1. Añadir libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Listar libros prestados")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        copias = int(input("Número de copias: "))
        añadir_libro(biblioteca, titulo, autor, copias)

    elif opcion == "2":
        titulo = input("Título del libro: ")
        prestar_libro(biblioteca, titulo)

    elif opcion == "3":
        titulo = input("Título del libro: ")
        devolver_libro(biblioteca, titulo)

    elif opcion == "4":
        listar_libros(biblioteca)

    elif opcion == "5":
        break

    else:
        print("Opción no válida")
