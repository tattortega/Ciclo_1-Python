#este programa seguira solicitando numeros hasta que ingrese un cero
numero=float(input("escriba un numero:"))
suma=0 #acumulador
contador=0 #contador
while numero !=0:
    suma += numero
    contador +=1
    print("la suma de los numeros es", suma)
    promedio=suma/contador
    print("el promedio es", promedio)
    if suma >100:
        print("pasaste de 100, ya no pedire mas numero")
        break

    numero=float(input("escriba un numero:"))
print("la suma de los numeros es", suma)

if contador>0:
    promedio=suma/contador
    print("el promedio es", promedio)
else:
    print("no puedo obtener un promedio dado que no ingresaste ningun numero diferente de cero")





