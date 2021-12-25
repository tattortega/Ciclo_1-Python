#este programa pide las notas de un curso y saca el promedio

num_notas = 0
while num_notas <= 0 or num_notas >=7:
    try:
        num_notas = int(input("¿Cuantas notas son? (entre 1 y 6) "))
    except ValueError:  
        num_notas = 0
#Ahora pido las notas
lista_nombres = []
lista_notas = []
for i in range(num_notas):
    lista_nombres.append(input("¿Cual es el tipo de nota? "))
    
    #Tengo que asegurarme de que me entreguen una nota entre 0 y 5
    nota_aux = -1
    while nota_aux <0 or nota_aux >5:
        try:
            nota_aux = float(input("¿Cual es la nota? "))
        except ValueError:
            nota_aux = -1
    lista_notas.append(nota_aux)

#sumo las notas
suma = 0
for nota_aux in lista_notas:
    suma +=nota_aux

#se imprimen las notas una a una
print("\n")
for i in range(len(lista_notas)):
    print(lista_nombres[i], lista_notas[i])

promedio = suma / len(lista_notas)
print("\nSu promedio es", promedio )











