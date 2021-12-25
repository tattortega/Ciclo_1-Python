#Programa para calcular comisiones


for i in range(0,3,1):
    nombre=input("Nombre: ")
    ventas=float(input("Ventas del mes: "))
    comision=ventas*0.25
    print("La comision es: $"'{:,}'.format(comision))

