# edwin, alex, sebas

import csv

with open("users_database.csv", 'r') as csv_file:
    data = list(csv.reader(csv_file))
    cintas = list(set([fila[1] for fila in data][1:]))
    for indice, cinta in enumerate(cintas):
        print(f"Opción #{indice} - {cinta}")
    seleccion = int(input(" Introduzca el número a elegir: "))
    for row in data:
        print(row)
        if row[1] == cintas[seleccion]:
            print(row)
