#Subsidio de vivienda

personas=5
for i in range(5):
    nombre=input("Nombre: ")
    cedula=(input("Cedula: "))
    ingreso_anual=float(input("Ingreso anual promedio: "))
    personas_cargo=int(input("Numero de personas a cargo: "))
    if ingreso_anual>24000000 and personas_cargo>=3:
        print("Puedes acceder al subsidio de vivienda")
        print("Nombre: ",nombre)
        print("Cedula: ",cedula)
    else:
        print("No puedes acceder al subsidio de vivienda")
        
