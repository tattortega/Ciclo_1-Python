#Factorial sin recursividad

def factorial(numeros):
    if numeros==0 or numeros==1:
        return 1
    else:
        fact=1
        for i in range(numeros,1,-1):
            fact=fact*i
        return fact

numeros=int(input("Ingrese numero: "))
fact=factorial(numeros)
print("Factorial: ",fact)


#Fatorial con recursividad

def factorial_recursivo(numero):
    if numero==0 or numero==1:
        return 1
    else:
        return numero*factorial_recursivo(numero-1)

numero=int(input("Ingrese numero: "))
facto=factorial_recursivo(numero)
print("Factorial: ",fact)
