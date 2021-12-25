#Crear archivo de texto

#Importar el modulo io
from io import open

#Fase de creacion y apertura
archivo_texto=open("nombres.txt","w")

#Fase de manipulacion
nom="Luis \nRicardo \nOrtega"
archivo_texto.write(nom)

#Fase de cierre
archivo_texto.close()


