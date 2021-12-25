#Leer archivo de texto linea a linea

#Importar el modulo io
from io import open

#Fase de apertura
archivo_texto=open("nombres.txt","r")

#Fase de manipulacion
lista_nombres=archivo_texto.readlines()

#Fase de cierre
archivo_texto.close()

print(lista_nombres)
for i in range(len(lista_nombres)):
    print(f"Nombre: {lista_nombres[i]}")


