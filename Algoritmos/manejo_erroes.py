print("este programa divide dos numeros")


try:
    numero1= int(input("escriba el dividendo: "))
    numero2= int(input("escriba el divisor: "))

    
    division= numero1/numero2
   
except ValueError:
    print("ha ocurrido un error")
except ZeroDivisionError:
    print("el divisor debe ser diferente de cero")
else:
    print("el resultado de la divison es", division)
finally:
    print("esto siempre ocurre")