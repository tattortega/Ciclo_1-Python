#crear un diccionario con los datos de una persona
persona = {
    "Nombres" : "Luis Ricardo",
    "Apellidos" : "Ortega Mantilla",
    "Telefono" : "123412421",
    "Edad" : 26,
    "Ciudad" : "Cucuta",
}
print(persona)

#acceder a los elementos de un diccionario por su nombre
print("El nombre de la persona es", persona["Nombres"])

#agregar una nueva variable al diccionario
nombre_llave = input("¿Cual es el nombre de la nueva llave?")
valor = input("¿Cual es su valor?")

persona[nombre_llave] = valor
print("la persona ha cambiado", persona)

#recorrer un diccionario
#imprimo las llaves
for x in persona:
    print(x)
    
for x in persona.keys():
    print(x)
    
#imprimo los valores de las llaves
for x in persona:
    print(persona[x])

for x in persona.values():
    print(x)














