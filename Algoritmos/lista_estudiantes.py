#este programa solicita los datos de varios estudiantes y los muestra en pantalla
cantidad = int(input("¿Cuantos estudiantes va a registrar?"))

lista_estudiantes = []
for i in range(cantidad):
    nombres = input("Nombres del estudiante numero" + str(i + 1))
    apellidos = input("Apellidos del estudiante numero" + str(i + 1))
    documento = input("Numero de documento del estudiante numero" + str(i + 1))
    edad = int(input("Edad del estudiante numero" + str(i + 1)))

    estudiante = [nombres, apellidos, documento, edad]

    lista_estudiantes.append(estudiante)
     
print("Listado de estudiantes: ")
for estudiantes in lista_estudiantes:
    print("Nombre", estudiante[1], ",", estudiante[0], "Documento", estudiante[2], "Edad", estudiante[3])

