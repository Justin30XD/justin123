# Pedir al usuario si quiere una pizza vegetariana o no
opcion = input("¿Quiere una pizza vegetariana? (s/n): ")

# Mostrar el menú de ingredientes disponibles según la elección del usuario
if opcion == "s":
    print("Ingredientes disponibles para pizza vegetariana:")
    print("1. Pimiento")
    print("2. Tofu")
else:
    print("Ingredientes disponibles para pizza no vegetariana:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")

# Pedir al usuario que elija un ingrediente
ingrediente = input("Elija un ingrediente (1-3): ")

# Definir los ingredientes de la pizza según la elección del usuario
if opcion == "s":
    tipo_pizza = "vegetariana"
    if ingrediente == "1":
        ingredientes = "pimiento"
    else:
        ingredientes = "tofu"
else:
    tipo_pizza = "no vegetariana"
    if ingrediente == "1":
        ingredientes = "peperoni"
    elif ingrediente == "2":
        ingredientes = "jamón"
    else:
        ingredientes = "salmón"

# Mostrar la pizza elegida
print("Pizza", tipo_pizza, "con mozzarella, tomate y", ingredientes)
