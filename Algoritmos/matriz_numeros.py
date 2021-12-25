#Programa para contar positivos,negatios y ceros de una matriz
#Autor=Ricardo Ortega
#Fecha:28/08/2021

numeros=[]
for i in range(0,2,1):
    numeros.append([])
    for  j in range(0,2,1):
        num=int(input("Ingrese numero: "))
        numeros[i].append(num)
cp=0
cn=0
cc=0
for i in range(2):
    for j in range(2):
        if  numeros[i][j]>0:
            cp+=1
        elif numeros[i][j]<0:
            cn+=1
        else:
            cc+=1
            
print(numeros)
print("Total de numeros positivos: ", cp,"\nTotal de numeros negativos: ", cn, "\nTotal de ceros: ",cc)
