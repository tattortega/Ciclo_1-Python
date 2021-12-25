print("Este programa divide dos números")

try:
    num1 = float(input("Escribe el dividendo: "))
    num2 = float(input("Escribe el divisor: "))

    division = num1 / num2
except ValueError as err:
    print("Los datos que entregues deben ser numéricos")
    print(err)
except ZeroDivisionError as err:
    print("El divisor debe ser diferente de cero")
    print(err)
else:
    print("El resultado de la división es", division)
finally:
    print("Esto siempre ocurre")
