print("este programa suma dos numeros")

bol_error= True
while bol_error:
    try:
        num1=float(input("Digita el primer numero"))
    except ValueError:
        print ("no es un numero valido")
    else:
        bol_error=False

bol_error= True
while bol_error:
    try:
        num2=float(input("Digita el segundo numero"))
    except ValueError:
        print ("no es un numero valido")
    else:
        bol_error=False

suma=num1+num2

print("la suma es ", suma)