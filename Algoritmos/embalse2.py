#Embalse del municipio de Tubara
respuesta="si"

while respuesta=="si" or respuesta=="Si" or respuesta=="SI":
    niv_act=float(input("Escriba el nivel actual del embalse (en metros):"))
    niv_aum=float(input("Escriba el aumento de nivel del embalse (en metros):"))
    niv_act +=niv_aum
    print("El nivel actual del embalse es:",niv_act, "metros")
    if niv_act==25:
        print("¡ALERTA! Los operarios pueden operar las compuertas de liberacion de agua")    
        respuesta= input("\n ¿Desea iniciar nuevamente el control del nivel de agua del embalse? (si/no)")
