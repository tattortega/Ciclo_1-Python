cantidad= int(input("¿cuantos numeros quieres ingresar?"))

#creo una lista vacia
lista_numeros=[]
print("Ingresa los numeros")
while len(lista_numeros) < cantidad:
    try:
        numero=int(input())
    except ValueError:
        print("no es un numero valido")
    else: 
        #agregar al final   
        lista_numeros.append(numero)
        
        #agregar en una posicion dada
        #lista_numeros.insert(0,numero)
print("los numeros entregados son", lista_numeros)

for indice in range(-1,-(cantidad +1),-1):
    print(lista_numeros[indice])

#reemplazar el elemento de una lista

lista_numeros[1]=0







