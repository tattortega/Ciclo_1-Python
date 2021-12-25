#Reto 4: Liquidación servicio de servicio de agua

#Definicion de funciones
def calcular_valor_pagar(estrato,lectura_mes_anterior,lectura_mes_actual):
    if estrato==1:
        tarifa_basica=20000
    elif estrato==2:
        tarifa_basica=30000
    elif estrato==3:
        tarifa_basica=45000
    elif estrato==4:
        tarifa_basica=60000
    else:
        tarifa_basica=80000
    valor_consumo=(lectura_mes_anterior-lectura_mes_actual)*500
    valor_pagar=abs(valor_consumo)+tarifa_basica
    return valor_pagar

def validar_estrato():
    while True:
        try:
            estrato=int(input("Ingrese estrato(1,2,3,4,5): "))
            if estrato<1 or estrato >5:
                print("El estrato debe ser de 1 a 5")
                continue
            break
        except ValueError:
            print("Debe ser un numero entero")
    return estrato


#Programa principal
suscriptores=int(input("Ingrese la cantidad de suscriptores: "))
valor_total=0
for i in range(suscriptores):
    nombre=input("Ingrese Nombre: ")
    estrato=validar_estrato()
    lectura_mes_anterior=int(input("Lectura del medidor del mes anterior en cm3: "))
    lectura_mes_actual=int(input("Lectura del medidor del mes actual en cm3: "))
    valor_pagar=calcular_valor_pagar(estrato,lectura_mes_anterior,lectura_mes_actual)
    valor_total+=valor_pagar
    print("Valor a pagar del suscriptor: $"'{:,.2f}'.format(valor_pagar))
print("Valor total a pagar de todos los suscriptores: $"'{:,.2f}'.format(valor_total))
