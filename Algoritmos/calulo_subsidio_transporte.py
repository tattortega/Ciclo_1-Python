#Programa para calcular subsidio de transporte

#Entrada
nombre=input("Nombre: ")
salario=float(input("Salario: "))

#Proceso
if salario<=900000:
    st=100000
else:
    st=0

#Salida
print("Nombre: ",nombre)
print("Salario: $"'{:,.2f}',salario)
print("Subsidio: $"'{:,.2f}',st)
