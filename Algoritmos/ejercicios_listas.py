#Ejercicios listas

#1
numeros=[53,23,8,32,86,132]
suma=0
for valor in numeros:
        suma+=valor
promedio=suma/len(numeros)
print("Promedio es : ",promedio)

#2
num=[425,845,33,5,23,53,76]
num.sort()
print("numero menor: ",num[0])
print("numero mayor: ",num[-1])

#3
a=[432,5,12,86,4,2]
b=[23,64,89,4,90,4]
c=[]
d=[]

for i in range(len(a)):
    c.append(a[i])
for i in range(len(b)):
    c[i]=c[i]+b[i]
    
for i in range(len(a)):
    d.append(a[i])
for i in range(len(b)):
    c[i]=c[i]-b[i]
        
print("Suma de lista a y b: ",c)
print("resta de la lista a y b",d)
print("unir las lista a y b: ",(a+b))
