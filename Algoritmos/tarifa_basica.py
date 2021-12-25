#Programa que calcula la tarifa basica de energia segun el estrato

#Entrada
nombre=input("Escriba el nombre: ")
estrato=int(input("Escriba el estrato: "))

#Proceso
tb=0
if estrato==1:
    tb=10000
elif estrato==2:
    tb=15000
elif estrato==3:
    tb=30000
elif estrato==4:
    tb=50000
elif estrato==5:
    tb=65000
        
#Salida
print("Nombre: ",nombre)
print("Estrato: ",estrato)
print("Tarifa basica: $",'{:,}'.format(tb))
