#Programa para contar vocales de una matriz
#Autor=Ricardo Ortega
#Fecha:28/08/2021

letras=[['u','i','x'],['e','t','m'],['a','w','o']]


cv=0

for i in range(3):
    for j in range(3):
        if  letras[i][j]=='a' or letras[i][j]=='e' or letras[i][j]=='i' or letras[i][j]=='o' or letras[i][j]=='u':
            cv+=1
print("Total de letras: ", cv)

letras=[]
for x in range(0,3,1):
    letras.append([])
    for  y in range(0,3,1):
        let=input("Ingrese letra: ")
        letras[x].append(let)
cv=0

for i in range(3):
    for j in range(3):
        if  letras[i][j]=='a' or letras[i][j]=='e' or letras[i][j]=='i' or letras[i][j]=='o' or letras[i][j]=='u':
            cv+=1
print(letras)
print("Total de letras: ", cv)
