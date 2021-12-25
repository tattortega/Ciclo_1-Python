#Agregar informacion al archivo de texto l

#Importar el modulo io
from io import open

#Fase de apertura
archivo_texto=open("nombres.txt","a")

#Fase de manipulacion
nom="\nBien"
archivo_texto.write(nom)

#Fase de cierre
archivo_texto.close()

print(archivo_texto)

