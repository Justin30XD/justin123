# Definimos el diccionario con los créditos de las asignaturas
creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# Mostramos por pantalla los créditos de cada asignatura
for asignatura, creditos_asignatura in creditos.items():
    print(f'{asignatura} tiene {creditos_asignatura} créditos')

# Calculamos el número total de créditos del curso
total_creditos = sum(creditos.values())

# Mostramos por pantalla el número total de créditos
print(f'El curso tiene un total de {total_creditos} créditos')
