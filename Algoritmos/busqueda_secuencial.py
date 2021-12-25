#Busqueda secuencial o lineal con funciones

def busqueda_lineal(numeros,buscar,posicion):
    for i in range(n):
        if numeros[i]==buscar:
            posicion.append(i)
    return posicion

numeros=[]
posicion=[]
n=int(input("Ingrese cantidad de elementos: "))
for i in range(n):
    num=int(input("Numeros: "))
    numeros.append(num)
print("Lista: ",numeros)

buscar=int(input("Informacion a buscar: "))

posicion=busqueda_lineal(numeros,buscar,posicion)

print("Lista con posiciones encontradas: ",posicion)

