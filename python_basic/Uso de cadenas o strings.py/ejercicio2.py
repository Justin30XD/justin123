def imprimir_nombre_completo(nombre_completo):
    # Imprimir nombre completo en minúsculas
    print(nombre_completo.lower())

    # Imprimir nombre completo en mayúsculas
    print(nombre_completo.upper())

    # Imprimir nombre completo con primera letra en mayúscula
    palabras = nombre_completo.split()
    nombre_apellidos = [palabra.capitalize() for palabra in palabras]
    nombre_apellidos = " ".join(nombre_apellidos)
    print(nombre_apellidos)

nombre_completo = input("Introduce tu nombre completo: ")
imprimir_nombre_completo(nombre_completo)
