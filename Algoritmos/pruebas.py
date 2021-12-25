lista_nit = ["325", "663452", "765543"]  
lista_proveedores = ["hola", "suma", "resta"] 
lista_cotizaciones = [30276540, 45140340, 35328970 ]    
    
menor = lista_cotizaciones [0]
indice_menor = 0
mayor = lista_cotizaciones [0]
indice_mayor = 0
for i in range(len(lista_cotizaciones)):
    if lista_cotizaciones[i] < menor:
        menor = lista_cotizaciones[i]
        indice_menor = i
for i in range(len(lista_cotizaciones)):    
    if lista_cotizaciones[i] > mayor:
        menor = lista_cotizaciones[i]
        indice_mayor = i

print("\nCotización más baja\n")
print("NIT: ", lista_nit[indice_menor])
print("Nombre: ", lista_proveedores[indice_menor])
print("Valor: ", lista_cotizaciones[indice_menor])

print("\nCotización más alta\n")
print("NIT: ", lista_nit[indice_mayor])
print("Nombre: ", lista_proveedores[indice_mayor])
print("Valor: "'{:,}'.format(lista_cotizaciones[indice_mayor]))
