def mostrar_numero_telefono(numero_telefono):
    numero_sin_prefijo = numero_telefono[4:14]
    numero_sin_ext = numero_sin_prefijo[:-3]
    print(numero_sin_ext)

# Ejemplo de uso
numero_telefono = "+34-4568399-56"
mostrar_numero_telefono(numero_telefono)
