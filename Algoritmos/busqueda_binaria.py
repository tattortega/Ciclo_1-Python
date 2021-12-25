#Busqueda binaria

def busqueda_binaria(vector,elemento):
    izq=0
    der=len(vector)-1
    while izq<=der:
        med=(izq+der)//2
        if elemento==vector[med]:
            return med
        elif vector[med]>elemento:
            der=med-1
        else:
            izq=med+1
    return -1

vector=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
elemento=int(input("Informacion a buscar: "))
pos=busqueda_binaria(vector,elemento)
if pos==-1:
    print("Informacion NO encontrada")
else:
    print("Informacion encontrada en la posicion: ",pos)


#Busqueda binaria con recursividad

def busqueda_binaria_recursiva(vectores,elementos,izqu,dere):    
    if izqu>dere:
        return -1
    else:
        med=(izqu+dere)//2
        if elementos==vectores[med]:
            return med
        elif vectores[med]>elementos:
            dere=med-1
            return busqueda_binaria_recursiva(vectores,elementos,izqu,dere)
        else:
            izqu=med+1
            return busqueda_binaria_recursiva(vectores,elementos,izqu,dere)

vectores=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
elementos=int(input("Informacion a buscar: "))
izqu=0
dere=len(vector)-1
posi=busqueda_binaria_recursiva(vector,elemento,izqu,dere)
if posi==-1:
    print("Informacion NO encontrada")
else:
    print("Informacion encontrada en la posicion: ",posi)
