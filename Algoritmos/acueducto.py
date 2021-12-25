print("Este programa calcula el nivel de agua del embalse")

respuesta="s"
while respuesta=="s" or respuesta =="S" or respuesta=="Si":
    nivel=float(input("Ingrese el nivel inicial del embalse: "))

    while nivel < 25:
        aumento= float(input("Ingrese el aumento de nivel de agua en metros: "))
        nivel +=aumento
        print("El nivel actual es", nivel)

    print("El embalse llego al limite, se procedera a abrir las compuertas de control")

    respuesta=input("¿Desea volver a ejecutar el programa? (si/no) ")





