#Crear archivo json partiendo de una lista

import json

#Estructura de datos
lista=[10,20,30,40,60]

#Fase de apertura y creacion
with open("lista.json","w") as archivo:
    json.dump(lista,archivo)



#Crear archivo json partiendo de un diccionario

import json

#Estructura de datos
diccionario={'1':'Lapiz',
       '2':'Borrador',
       '3':'Cuaderno',
       '4':'Lapicero'
       }

#Fase de apertura y creacion
with open("diccionario.json","w") as archivo:
    json.dump(diccionario,archivo)
