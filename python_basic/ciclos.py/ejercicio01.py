cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
anios = int(input("Ingrese el número de años de la inversión: "))

interes_decimal = interes_anual / 100
capital = cantidad

for i in range(anios):
    capital += capital * interes_decimal
    print("Capital obtenido en el año {}: {:.2f}".format(i+1, capital))
