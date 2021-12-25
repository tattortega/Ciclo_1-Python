def particion(vector):
    pivote=vector[0]
    menores=[]
    mayores=[]
    for i in range(1,len(vector)):
        if vector[i]<pivote:
            menores.append(vector[i])
        else:
            mayores.append(vector[i])
    return menores,pivote,mayores

def quicksort(vector):
    if len(vector)<2:
        return vector
    else:
        menores,pivote,mayores=particion(vector)
    return quicksort(menores) + [pivote] + quicksort(mayores)


vector=[7,2,6,3,5,1,9,4,8]
print("Lista original: ",vector)
vector=quicksort(vector)
print("Lista ordenada: ", vector)
