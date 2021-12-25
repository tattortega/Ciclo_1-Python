#Programa para calcular tarifa basica de servicio telefonico usando funciones

#Definicion de funciones
#def nombre_funcion(parametros de entrada)
def calcular_valor_pagar(estrato,impulsos):
    if estrato==1:
        tarifa_basica=10000
    elif estrato==2:
        tarifa_basica=15000
    elif estrato==3:
        tarifa_basica=20000
    elif estrato==4:
        tarifa_basica=25000
    else:
        tarifa_basica=30000
    valor_impulsos=impulsos*100
    valor_pagar=tarifa_basica+valor_impulsos
    return valor_pagar

#Programa principal
abonados=int(input("Ingrese la cantidad de abonados: "))
valor_total=0
for i in range(abonados):
    nombre=input("Nombre: ")
    estrato=int(input("Estrato(1,2,3,4,5): "))
    impulsos=int(input("Impulsos del mes: "))
    valor_pagar=calcular_valor_pagar(estrato,impulsos)
    valor_total+=valor_pagar
    print("Valor a pagar abonado: $"'{:,.2f}'.format(valor_pagar))
print("Valor total facturacion: $"'{:,.2f}'.format(valor_total))
