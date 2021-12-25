#Empresa TRASRAPIDO

conductores=4
for i in range(0,4):
    cedula=input("Cedula: ")
    nombre=input("Nombre: ")
    direccion=input("Direccion: ")
    telefono=int(input("Telefono: "))
    clase_conductor=input("Clase de conductor \nExperto(E)\nNovato(N)\n")
    pasajes_mes=float(input("Valor total por concepto de pasajes del mes: "))
    encomiendas_mes=float(input("Valor total por concepto de encomiendas del mes: "))
    if clase_conductor=="E":
        comision=(pasajes_mes*0.30)+(encomiendas_mes*0.20)
        print("Nombre: ",nombre)
        print("Comisiones a pagar: $",'{:,.2f}'.format(comision))
    else:
        clase_conductor=="N"
        comision=(pasajes_mes*0.20)+(encomiendas_mes*0.15)
        print("Nombre: ",nombre)
        print("Comisiones a pagar: $",'{:,.2f}'.format(comision))        
