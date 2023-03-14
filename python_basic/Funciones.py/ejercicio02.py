def decimal_a_binario(numero):
    """
    Función que convierte un número decimal en binario.

    :param numero: El número decimal a convertir.
    :return: El número binario como una cadena de caracteres.
    """
    # Caso base: el número es cero
    if numero == 0:
        return '0'

    # Lista para almacenar los dígitos binarios
    digitos_binarios = []

    # Convertimos el número a binario
    while numero > 0:
        # Añadimos el dígito binario correspondiente al inicio de la lista
        digito_binario = numero % 2
        digitos_binarios.insert(0, str(digito_binario))

        # Dividimos el número entre 2 y redondeamos hacia abajo
        numero //= 2

    # Concatenamos los dígitos binarios y devolvemos el resultado
    numero_binario = ''.join(digitos_binarios)
    return numero_binario


def binario_a_decimal(numero):
    """
    Función que convierte un número binario en decimal.

    :param numero: El número binario a convertir (como una cadena de caracteres).
    :return: El número decimal.
    """
    # Convertimos la cadena de caracteres a una lista de dígitos binarios
    digitos_binarios = list(numero)

    # Convertimos cada dígito binario a su valor decimal y lo sumamos
    numero_decimal = 0
    for indice, digito_binario in enumerate(digitos_binarios):
        potencia = len(digitos_binarios) - indice - 1
        numero_decimal += int(digito_binario) * 2 ** potencia

    # Devolvemos el resultado
    return numero_decimal

# Convertir un número decimal a binario
numero_binario = decimal_a_binario(42)
print(numero_binario)  # Debe mostrar '101010'

# Convertir un número binario a decimal
numero_decimal = binario_a_decimal('110110')
print(numero_decimal)  # Debe mostrar 42

