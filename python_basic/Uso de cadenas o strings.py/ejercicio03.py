def mostrar_longitud_nombre(nombre):
    nombre_mayusculas = nombre.upper()
    longitud_nombre = len(nombre)
    print(nombre_mayusculas + " tiene " + str(longitud_nombre) + " letras")

# Ejemplo de uso
nombre = input("Introduce tu nombre: ")
mostrar_longitud_nombre(nombre)
