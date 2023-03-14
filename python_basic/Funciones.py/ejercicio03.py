def contar_palabras(cadena):
    """
    Función que cuenta la frecuencia de cada palabra en una cadena de caracteres.

    :param cadena: La cadena de caracteres a analizar.
    :return: Un diccionario que mapea cada palabra a su frecuencia.
    """
    # Dividimos la cadena en palabras
    palabras = cadena.split()
    frecuencias = {}

    # Contamos la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    # Devolvemos el diccionario con las frecuencias
    return frecuencias


def palabras(diccionario):
    """
    Función que devuelve la palabra más común y su frecuencia en un diccionario.

    :param diccionario: El diccionario que mapea cada palabra a su frecuencia.
    :return: Una tupla con la palabra más común y su frecuencia.
    """
    # Encontramos la palabra con la mayor frecuencia
    palabras = None
    frecuencia_maxima = 0
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_maxima:
            palabras = palabra
            frecuencia_maxima = frecuencia

    # Devolvemos una tupla con la palabra más común y su frecuencia
    return (palabras, frecuencia_maxima)

# Contar la frecuencia de cada palabra en una cadena
cadena = 'Hola gente bella de python me llamo justin'
frecuencias = contar_palabras(cadena)
print(frecuencias)  

# Encontrar la palabra más común en un diccionario de frecuencias
palabra_comun, frecuencia = palabras(frecuencias)
print(palabra_comun, frecuencia)  
