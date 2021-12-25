#Programa para calcular la nota definitiva de un tripulante en un ciclo

#Entrada
nr1=float(input("Nota reto 1: "))
nr2=float(input("Nota reto 2: "))
nr3=float(input("Nota reto 3: "))
nr4=float(input("Nota reto 4: "))
nr5=float(input("Nota reto 5: "))
ni=float(input("Nota Ingles: "))

#Proceso
nd=nr1*0.1+nr2*0.1+nr3*0.2+nr4*0.2+nr5*0.2+ni*0.2

#salida
print("Nota definitiva: ",nd)
