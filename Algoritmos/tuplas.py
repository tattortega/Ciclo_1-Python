mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6)
mi_lista.insert(0, 10)
mi_lista[0] = 0
print(mi_lista)

mi_tupla = (1, 2, 3, 4, 5)
mi_tupla2 = mi_tupla
#mi_tupla.append(6) la tupla no tiene append
#mi_tupla.insert(0, 10) la tupla no tiene insert
#mi_tupla[0] = 0 la tupla no tiene asignacion de indice
mi_tupla = (10, 20, 30)
print(mi_tupla)
print(mi_tupla2)

#puedo acceder al contenido de la tupla
print(mi_tupla[-1])

#guardar listas dentro de una tupla
mi_tupla3 = ([1, 2, 3], [5, 6, 7, 8], [10, 12, 9, 11]) 
print(mi_tupla3)
print(mi_tupla3[2][1])

#modificar los valores de las listas dentro de tuplas
mi_tupla3[0].append(4)
mi_tupla3[2].insert(2, 13) 
print(mi_tupla3)
mi_tupla3[1].clear()
print(mi_tupla3)

#crear una tupla con un solo elemento
mi_tupla4 = (5,)
print(mi_tupla4[0])





