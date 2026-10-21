# Algoritmo SistemaGestionEscolar

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
    print("")
    print("Nombre: ", nombre)
    print("Curso: ", curso)
