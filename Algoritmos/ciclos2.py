#ahora vamos a sumar solamente los pares pero filtrando con un if
numero=int (input("¿hasta que numero quieres sumar?"))
suma=0 #este es un acumulador
cuenta=0 #este es un contador

for i in range(numero+1):
    if i>0 and i%2==0:
        suma +=i
        cuenta +=1

print("la suma de los numeros pares es:",suma)
print("el ciclo se ejecuto",cuenta, "veces")


#voy a solicictar 5 numeros para sumarlos pero si escribes 0 me detendre y dare la respuesta
suma2=0 #acumulador
contador=0 #contador
for i in range(5):
    numero=int (input("dame un numero que no sea cero:"))
    if numero !=0:
        suma2=suma2 +numero
        contador=contador+1
    else:
        print("te lo dije")
        break


print(contador)
print("la suma es",suma2)
if contador>0:
    promedio=suma2 / contador
    print("el promedio es",promedio) 
else:
    print("no se puede calcular el promedio")





