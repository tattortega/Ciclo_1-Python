#ejercicio calcular valor compra articulos

articulos={
    1:'arroz',
    2:'aceite',
    3:'harina',
    4:'lenteja',
    5:'frijol'   
    }
precios={
    1:3000,
    2:2500,
    3:2800,
    4:1500,
    5:1700
    }
n=int(input("Cantidad de articulos: "))
vt=0
for i in range(n):
    cod=int(input("Codigo articulo: "))
    cant=int(input("Cantidad de articulos: "))
    vart=cant*precios[cod]
    vt=vt+vart
    print("Codigo del articulo: ",cod)
    print("Nombre del articulo: ",articulos[cod])
    print("Precio unitario del articulo: $",'{:,}'.format(precios[cod]))
    print("Valor compra del articulo: $",'{:,}'.format(vart))
print("Valor total de la compra: $",'{:,}'.format(vt))


    
    
    
    
