#creo una lista
milista = [5, 14, 9, -3, 0]
print(milista)

#agrego -25 al final
milista.append(-25)
print(milista)

#agrego 14 en la posicion de indice 3
milista.insert(3, 14)
print(milista)

#reemplazo el valor de indice 3 por 15
milista[3] = 15
print(milista)

#reemplazo un texto en el indice 2
milista[2] = "hola, me llamo luis"
print(milista)

#reemplazo el indice 4 por una lista
milista[4] = ["a", "b", "c"]
print(milista)

#matriz
print("\nAhora voy a trabajar con matrices")
mimatriz = []
mimatriz.append([1, 6, 11, 16])
mimatriz.append([2, 7, 12, 27])
mimatriz.append([3, 8, 13, 18])
mimatriz.append([4, 9, 14, 19])
mimatriz.append([5, 10 , 15, 20])
print(mimatriz)

mimatriz2 = [[1, 6, 11, 16], [2, 7, 12, 27], [3, 8, 13, 18], [4, 9, 14, 19], [5, 10 , 15, 20]]
print(mimatriz2)


print("Voy a hallar el valor de la fila 2 columna 3: ", mimatriz[2][3])

#reemplazar el primer valor de toda la matriz  y el ultimo por ceros
mimatriz[0][0] = 0
mimatriz[-1][-1] = 0
print(mimatriz)

#agregar una nueva fila
mimatriz.append([41, 42, 43, 44])
print(mimatriz)

#mimatriz.insert([1, 2][1, 2, 3, 4])
# print(mimatriz)

#agregar una columna con todos los valores igual a 10
for fila in mimatriz:
    fila.append (10)
print(mimatriz)

#sumar todos los valores de la matriz
suma = 0
for fila in mimatriz:
    for valor in fila:
        suma += valor

print(suma)
