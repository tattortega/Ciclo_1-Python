#Metodo burbuja con funciones

def valida_entero(mensaje):
    while True:
        try:
            dato = int(input(mensaje))
            break
        except ValueError:
            print("Error! El dato debe ser entero Intenta de nuevo...")
    return dato

def ordenamiento_burbuja(numeros):
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if numeros[i]>numeros[j]:
                #t=numeros[i]
                #numeros[i]=numeros[j]
                #numeros[j]=t
                numeros[i],numeros[j]=numeros[j],numeros[i]
    return numeros
            
n=valida_entero("Ingrese cantidad de elementos: ")
numeros=[]
for i in range(n):
    num=valida_entero("Numeros: ")
    numeros.append(num)

print(numeros)
print("Lista ordenada ascendentemente: ",ordenamiento_burbuja(numeros))
        
    
