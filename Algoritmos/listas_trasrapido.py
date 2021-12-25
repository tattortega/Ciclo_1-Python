#Lista de TRASRAPIDO


nombres=[]
categoria=[]
pasajes=[]
encomiendas=[]

n=int(input("Cantidad de conductores: "))
for i in range(n):
    nombres.append(input("Nombre: "))
    categoria.append(input("Categoria: "))
    pasajes.append(float(input("Valor pasajes: ")))
    encomiendas.append(float(input("Valor encomiendas: ")))
for j in range(n):
    if categoria[j]=='N':
        vp=pasajes[x]*0.2
        ve=encomiendas[x]*0.15
    else:
        vp=pasajes[j]*0.3
        ve=encomiendas[j]*0.2
    total=vp+ve
    print("Conductor: ",nombres[j])
    print("Valor total a pagar: ",total)
