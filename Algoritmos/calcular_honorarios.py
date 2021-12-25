#Calcular honorarios de docentes

codigo=int(input("Escribir codigo del docente: "))
while codigo!=999:   
    nombre=input("Ingrese nombre del docente: ")
    while True:
        try:
            categoria=int(input("Ingrese categoria del docente: "))
            if categoria<1 or categoria >3:
                print("Categoria debe ser 1,2 o 3")
                continue
            break
        except ValueError:
            print("La categoria debe ser entero")
    horas=float(input("Ingrese horas laboradas: "))
    if categoria==1:
        honorarios=horas*35000
    elif categoria==2:
        honorarios=horas*40000
    else:
        honorarios=horas*50000
    print("Honorarios: "'{:,}'.format(honorarios))
    codigo=int(input("Escribir codigo del docente: "))
print("Proceso finalizado")

