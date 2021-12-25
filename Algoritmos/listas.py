#crearemos una lista vacia
lista_vacia = []

#crearemos una lista con elementos
lista_numeros= [1,3,5]

# imprimir listas
print(lista_vacia)
print(lista_numeros)

print("segundo elemento de la lista no vacia", lista_numeros[1])

#solicitar una posicion que no exista
try:
    print("esta posicion de la lista no existe", lista_numeros[5])
except  IndexError as err:
    print("ha ocurrido un error", err)

#solicitar el ultimo elemento de la lista
print("el ultimo elemento es", lista_numeros[-1])

