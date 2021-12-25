#Reto 3: Operaciones entre conjuntos


n=[]
m=[]

for i in range(5):
    n.append(input("Ingrese elemento del conjunto A: "))
for i in range(5):
    m.append(input("Ingrese elemento del conjunto B: "))

a=set(n)
b=set(m)

#interseccion
c=[a&b]

#union
d=[a|b]

#diferencia
e=[a-b]

#diferencia simetrica
f=[a^b]
   
print("Lista N: ",n)
print("Lista M: ",m)
print("Operación Intersección (A n B): ",c)
print("Operación Unión (A u B): ",d)
print("Operación Diferencia (A – B): ",e)
print("Operación Diferencia simétrica (A Δ B): ",f)
    
