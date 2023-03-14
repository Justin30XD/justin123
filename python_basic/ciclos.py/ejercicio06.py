# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista para almacenar las notas
notas = []

# Solicitar la nota para cada asignatura
for asignatura in asignaturas:
    nota = float(input("Ingrese la nota de {}: ".format(asignatura)))
    notas.append(nota)

# Imprimir las notas para cada asignatura
for i in range(len(asignaturas)):
    print("En {} has sacado {}".format(asignaturas[i], notas[i]))
