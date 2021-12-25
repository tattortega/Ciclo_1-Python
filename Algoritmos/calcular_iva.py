#Programa para calcular el valor de iva de una compra
#Autor:Ricardo Ortega

#Entrada
vc=float(input("Ingrese el valor de compra: "))

#Proceso
iva=vc*0.19
vt=vc+iva

#salida
print("El valor de la compra es: ",vc)
print("El valor del iva es: ",iva)
print("El valor total es: ",vt)
