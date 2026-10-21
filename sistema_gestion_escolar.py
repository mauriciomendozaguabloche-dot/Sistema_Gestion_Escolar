# Algoritmo SistemaGestionEscolar

suma_promedios = 0

print("SISTEMA DE GESTION ESCOLAR")

# Repetir ... Hasta Que cantidad > 0
while True:
    cantidad = int(input("Ingrese la cantidad de estudiantes: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero. Intente de nuevo.")
    if cantidad > 0:
        break

for i in range(1, cantidad + 1):
    print("Estudiante ", i, " de ", cantidad)
    nombre = input("Ingrese el nombre del estudiante: ")
    curso = input("Ingrese el curso: ")

    while True:
        nota1 = float(input("Ingrese la nota 1 (0 a 20): "))
        if nota1 < 0 or nota1 > 20:
            print("Nota invalida. Debe estar entre 0 y 20.")
        if 0 <= nota1 <= 20:
            break

    while True:
        nota2 = float(input("Ingrese la nota 2 (0 a 20): "))
        if nota2 < 0 or nota2 > 20:
            print("Nota invalida. Debe estar entre 0 y 20.")
        if 0 <= nota2 <= 20:
            break

    while True:
        nota3 = float(input("Ingrese la nota 3 (0 a 20): "))
        if nota3 < 0 or nota3 > 20:
            print("Nota invalida. Debe estar entre 0 y 20.")
        if 0 <= nota3 <= 20:
            break

    while True:
        asistencias = int(input("Cuantas veces asistio a clases esta semana (0 a 5): "))
        if asistencias < 0 or asistencias > 5:
            print("Valor invalido. Debe estar entre 0 y 5.")
        if 0 <= asistencias <= 5:
            break

    promedio = (nota1 + nota2 + nota3) / 3
    suma_promedios = suma_promedios + promedio
    print("")
    print("Nombre: ", nombre)
    print("Curso: ", curso)
    print("Promedio: ", round(promedio, 2))
