#Recuperar la informacion de un archivo json(lista)

import json

with open("lista.json","r") as archivo:
    lista=json.load(archivo)

archivo.close()

print("lista: ",lista)

for i in range(len(lista)):
    print(lista[i])

#Recuperar la informacion de un archivo json(diccionario)

import json

with open("diccionario.json","r") as archivo:
    diccionario=json.load(archivo)

archivo.close()

print("diccionario: ",diccionario)

print(diccionario["2"])
