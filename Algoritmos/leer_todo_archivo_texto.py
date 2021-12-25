#Leer todo el archivo de texto

#Importar el modulo io
from io import open

#Fase de creacion y apertura
archivo_texto=open("nombres.txt","r")

#Fase de manipulacion
texto=archivo_texto.read()

#Fase de cierre
archivo_texto.close()

print(texto)


