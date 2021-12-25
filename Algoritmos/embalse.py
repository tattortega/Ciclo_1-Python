#Embalse del municipio de Tubara
niv_act=float(input("Escriba el nivel actual del embalse (en metros):"))

niv_aum=float(input("Escriba el aumento de nivel del embalse (en metros):"))

niv_tot=niv_act+niv_aum

while niv_tot:
    print("El nivel actual del embalse es:",niv_tot, "metros")
    niv_aum=float(input("Escriba el aumento de nivel del embalse (en metros):"))
    niv_tot +=niv_aum
    if niv_tot>=25:
        print("El nivel actual del embalse es:",niv_tot, "metros")
        print("¡ALERTA! Los operarios pueden operar las compuertas de liberacion de agua")    
        break







