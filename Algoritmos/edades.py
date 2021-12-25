print("Fecha de nacimiento")
año_nac = int(input("Año: "))
mes_nac = int(input("Mes: "))
dia_nac = int(input("Día: "))

#Se valida que la fecha de nacimiento sea correcta
bol_fecha_correcta = False
if año_nac > 0:
    if mes_nac > 0 and mes_nac <= 12:
        maximo_dias = 31
        if mes_nac == 4 or mes_nac == 6 or mes_nac == 9 or mes_nac == 11:
            maximo_dias = 30
        else:
            if mes_nac == 2:
                if año_nac % 4 == 0:
                    #Es bisiesto
                    maximo_dias = 29
                else:
                    #No es bisiesto
                    maximo_dias = 28
                
        #Validar el día
        if dia_nac > 0 and dia_nac <= maximo_dias:
            print("Fecha correcta")
            bol_fecha_correcta = True
        else:
            print("El día es incorrecto")
    else:
        print("El mes es incorrecto")
else:
    print("El año es incorrecto")

#Necesito saber si la fecha de nacimiento está bien o no
if bol_fecha_correcta:
    #La fecha de nacimiento está bien, pido la otra fecha
    print("\nFecha de toma de la prueba PCR")
    año_pcr = int(input("Año: "))
    mes_pcr = int(input("Mes: "))
    dia_pcr = int(input("Día: "))

    #Se valida que la fecha de nacimiento sea correcta
    bol_fecha_correcta = False
    if año_pcr >= 2020:
        if mes_pcr > 0 and mes_pcr <= 12:
            maximo_dias = 31
            if mes_pcr == 4 or mes_pcr == 6 or mes_pcr == 9 or mes_pcr == 11:
                maximo_dias = 30
            else:
                if mes_pcr == 2:
                    if año_pcr % 4 == 0:
                        #Es bisiesto
                        maximo_dias = 29
                    else:
                        #No es bisiesto
                        maximo_dias = 28
                    
            #Validar el día
            if dia_pcr > 0 and dia_pcr <= maximo_dias:
                print("Fecha correcta")
                bol_fecha_correcta = True
            else:
                print("El día es incorrecto")
        else:
            print("El mes es incorrecto")
    else:
        print("El año es incorrecto")

    #Se verifica si la fecha PCR es correcta
    if bol_fecha_correcta:
        #Las dos fechas son correctas, se procede a hacer el cálculo de la edad
        if mes_nac < mes_pcr:
            #Ya cumplió años
            edad = año_pcr - año_nac
        elif mes_nac > mes_pcr:
            #No ha cumplido años
            edad = año_pcr - año_nac - 1
        elif dia_nac <= dia_pcr:
            #Ya cumplí años o los estoy cumpliendo hoy
            edad = año_pcr - año_nac
        else:
            #Aunque estoy en el mes de mi cumpleaños, aún no he cumplido
            edad = año_pcr - año_nac - 1

        print("La edad de la persona es", edad, "años")
    else:
        #La fecha está mal
        print("Debes volver a iniciar el programa")
else:
    #La fecha está mal
    print("Debes volver a iniciar el programa")