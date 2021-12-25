#diccionario de ciudades
ciudades = {
    "68001" : "bucaramanga",
    "68276" : "floridablanca",
    "11001" : "bogota",
    "11001" : "medellin",
    "05001" : "cucuta",
    "63001" : "armenia",
    "66001" : "pereira",
}

repetir ="s"

while repetir=="s":
    codigo = input("Dime el cogido de la ciudad: ")
    try:    
        ciudad = ciudades[codigo]
        print("la ciudad es", ciudad)
    except KeyError:
        print("No tengo registrado ese codigo en la base de datos")
    
        repuesta = input("¿Quieres agregar el municipio? (s/n)")
        if repuesta == "s":
            ciudad = input("Nombre del municipio: ")
            ciudades[codigo] = ciudad
    repetir =  input("¿Quieres consultar oto codigo? (s/n)")    








