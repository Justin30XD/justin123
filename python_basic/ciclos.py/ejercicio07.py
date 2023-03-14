# Definimos la lista de asignaturas
asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

# Creamos un diccionario para almacenar las notas del usuario
notas = {}

# Pedimos al usuario que introduzca la nota de cada asignatura
for asignatura in asignaturas:
    nota = float(input(f'Introduce la nota de {asignatura}: '))
    notas[asignatura] = nota

# Creamos una lista para almacenar las asignaturas aprobadas
aprobadas = []

# Eliminamos de la lista de asignaturas las aprobadas y las añadimos a la lista de aprobadas
for asignatura, nota in notas.items():
    if nota >= 100:
        asignaturas.remove(asignatura)
        aprobadas.append(asignatura)

# Mostramos por pantalla las asignaturas que el usuario tiene que repetir
print('Tienes que repetir las siguientes asignaturas:')
for asignatura in asignaturas:
    print(asignatura)
