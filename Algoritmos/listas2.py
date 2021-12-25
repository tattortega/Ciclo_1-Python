mi_lista= [2,3,7,2,5,7,2,9]
mi_copia= mi_lista[:]
print(mi_lista)
num1=5
num2=num1

#leer un valor especifico
#primer elemento
print(mi_lista[0]) 
#segundo elemento
print(mi_lista[1])
#ultimo elemento
print(mi_lista[-1])
#penultimo elemento
print(mi_lista[-2])

#exraer una parte de la lista
parte= mi_lista[3:]
print("parte de una lista", parte)

#invertir una lista
mi_lista.reverse()
print("lista invertida", mi_lista)

#ordenar una lista
mi_lista.sort()
print("lista ordenada",mi_lista)
print("copia de la lista original", mi_copia)

num1=12
print(num1, num2)

#quitar elementos de la lista

#reemplazar contenido
mi_lista[2]=0
print("lista con el tercer elemento reemplazado", mi_lista)

#una posicion especifica
del mi_lista[2]
print("lista sin el tercer elemento", mi_lista)

#quitar un elemento por su valor, quitaremos el siete
mi_lista.remove(7)
print("lista sin el 7", mi_lista)

#dado que al tratar de borrar un elemento que no esta en la lista se debe capturar el error
try:
    mi_lista.remove(11)
except ValueError:
    print("el elemento 11 no esta en la lista")
print("lista sin el 11", mi_lista)

#sumar los elementos de la lista
suma=0
for i in range(len(mi_lista)):
    suma+=mi_lista[i]
print("la suma de los elementos de la lista es", suma)
 
#ahora recorramos la lista con un for ich
suma=0
for valor in mi_lista:
    suma+=valor
print("la suma de los elementos de la lista es", suma)


