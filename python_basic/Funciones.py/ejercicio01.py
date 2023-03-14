def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    """
    Función que calcula el total de una factura tras aplicarle el IVA.

    :param cantidad_sin_iva: La cantidad de la factura sin IVA.
    :param porcentaje_iva: El porcentaje de IVA a aplicar (por defecto, 21%).
    :return: El total de la factura con IVA.
    """
    cantidad_con_iva = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return cantidad_con_iva

# Calcular el total de una factura con un 10% de IVA
total = calcular_total_factura(100, 10)
print(total)

# Calcular el total de una factura con el IVA por defecto (21%)
total = calcular_total_factura(100)
print(total)
