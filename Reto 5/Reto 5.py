#Reto 5 Campeonato de futbol

def calcular_puntos(pg,pe):
    pt=partidos_ganados*3+partidos_empatados*1
    return pt           

def tabla_ordenada(equipos,pg,pe,pp,pt):
    for i in range(0,cant_equipos-1,1):
        for j in range(i+1,cant_equipos,1):
            if pt[i]<=pt[j]:               
                equipos[i],equipos[j]=equipos[j],equipos[i]       
                pg[i],pg[j]=pg[j],pg[i]
                pe[i],pe[j]=pe[j],pe[i]
                pp[i],pp[j]=pp[j],pp[i]
                pt[i],pt[j]=pt[j],pt[i]                
    return equipos,pg,pe,pp,pt

cant_equipos=int(input("Ingrese la cantidad de equipos del campeonato: "))
equipos=[]
pg=[]
pe=[]
pp=[]
pt=[]
for i in range(cant_equipos):
    equipo=input("Equipo: ")
    partidos_ganados=int(input("Partidos ganados: "))
    partidos_empatados=int(input("Partidos empatados: "))
    partidos_perdidos=int(input("Partidos perdidos: "))
    equipos.append(equipo)
    pg.append(partidos_ganados)
    pe.append(partidos_empatados)
    pp.append(partidos_perdidos)
    pt.append(calcular_puntos(pg,pe))
    
equipos,pg,pe,pp,pt=tabla_ordenada(equipos,pg,pe,pp,pt)

print("\nTabla de posiciones")
for i in range(cant_equipos):
    print("\nEquipo: ",equipos[i])
    print("Puntos: ",pt[i])
    print("Partidos ganados: ",pg[i])
    print("Partidos empatados: ",pe[i])
    print("Partidos perdidos: ",pp[i])
