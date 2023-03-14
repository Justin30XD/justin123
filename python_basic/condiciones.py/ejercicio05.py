puntuacion = float(input("Introduce la puntuación del empleado: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    cantidad = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    cantidad = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    cantidad = 2400 * puntuacion
else:
    print("Puntuación inválida.")
    nivel = ""
    cantidad = 0

if nivel != "":
    print("El nivel de rendimiento es", nivel, "y la cantidad de dinero recibida es de", cantidad, "euros.")
