#Reto 2:Liquidacion servicio de matricula

codigo=int(input("Escriba el código del estudiante: "))
while codigo <999:
    nombre=input("Nombre del estudiante: ")
    print("Programa académico al cual pertenece")
    prog_academ=int(input("1.Técnico en Sitemas\n2.Técnico en Desarrollo de Videojuegos\n3.Técnico en Animación Digital\n"))
    print("Indicador de beca")
    ind_beca=int(input("1.Beca por rendimiento académico\n2.Beca Cultural-Deportes\n3.Sin Beca\n"))
    if prog_academ==1:
        if ind_beca==1:
            matricula=800000
            descuento=matricula*0.50
            valor_neto=matricula-descuento
        elif ind_beca==2:
            matricula=800000
            descuento=matricula*0.40
            valor_neto=matricula-descuento
        else:
            matricula=800000
            descuento=0
            valor_neto=matricula
    if prog_academ==2:
        if ind_beca==1:
            matricula=1000000
            descuento=matricula*0.50
            valor_neto=matricula-descuento
        elif ind_beca==2:
            matricula=1000000
            descuento=matricula*0.40
            valor_neto=matricula-descuento
        else:
            matricula=1000000
            descuento=0
            valor_neto=matricula
    if prog_academ==3:
        if ind_beca==1:
            matricula=1200000
            descuento=matricula*0.50
            valor_neto=matricula-descuento
        elif ind_beca==2:
            matricula=1200000
            descuento=matricula*0.40
            valor_neto=matricula-descuento
        else:
            matricula=1200000
            descuento=0
            valor_neto=matricula
    print("Codigo: ",codigo)
    print("Nombre: ",nombre)
    print("Valor de matricula: $"'{:,.2f}'.format(matricula))
    print("Valor de descuento por beca: $"'{:,.2f}'.format(descuento))
    print("Valor neto a pagar: $"'{:,.2f}'.format(valor_neto))
    codigo=int(input("Escriba el código del estudiante: "))
