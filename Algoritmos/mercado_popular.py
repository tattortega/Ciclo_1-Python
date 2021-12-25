#Programa de la empresa Mercado Popular

vendedores=5
for i in range(5):
    nombre=input("Nombre del vendedor: ")
    tipo_vendedor=int(input("Tipo de vendedor \n1.Mayorista \n2.Minorista\n "))
    valor_ventas=float(input("Valor total de ventas: "))
    if tipo_vendedor==1:
        comision=valor_ventas*0.25
    else:
        tipo_vendedor==2
        comision=valor_ventas*0.15
    print("La comision es: ",'{:,.2f}'.format(comision))
    
        
