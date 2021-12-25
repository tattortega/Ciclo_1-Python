#dados los puntos de un poligogo hhalar su permitro
lista_x = [1, 2, 1, 3, 4, 5, 6]
lista_y = [1, 5, 7, 8, 6, 6, 1]

perimetro = 0
indice = 0
for x in lista_x:
    y = lista_y[indice]
    indice_sig = indice + 1
    try:
        x_sig = lista_x[indice_sig]
        y_sig_ = lista_y[indice_sig]
    except IndexError:
        indice_sig = 0
        x_sig = lista_x[indice_sig]
        y_sig_ = lista_y[indice_sig]
    lado = ((x - x_sig)**2 + (y -  y_sig_)**2)**0.5
    perimetro += lado

    indice += 1

print("El perimetro es", perimetro)













