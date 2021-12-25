print("fecha de nacimiento")
año_nac= int(input("Año: "))
mes_nac= int(input("Mes: "))
dia_nac= int(input("Dia: "))

#se valida que la fecha de nacimiento es correcta
in_fecha_correcta= False
if año_nac>0:
    if mes_nac>0 and mes_nac<=12:
        maximo_dias=31
        if mes_nac==1 or mes_nac==3 or mes_nac==5 or mes_nac==7 or mes_nac==8 or mes_nac==10 or mes_nac==12:
           maximo_dias=30
        else:
            if mes_nac==2:
                if año_nac%4==0:
                    if año_nac%400==0:
                        #si es bisiesto
                        maximo_dias=29
                    else:
                        if año_nac%100==0:
                            #año no es bisiesto
                            maximo_dias=28
                        else:
                            #no es divisible por 100, es bisiesto
                            maximo_dias=29
                else:    
                    #año no es bisiesto
                        maximo_dias=28
        #validar el dia
        if dia_nac>0 and dia_nac<=maximo_dias:
            print("la fecha es correcta")
            in_fecha_correcta=True
        else:
            print("el dia es incorrecto")
    else:
        print("la fecha es incorrecta")
        
else:
    print("el año es incorrecto")
    

if in_fecha_correcta:
    #la fecha es correcta
    print("\nFecha de toma de la prueba PCR")
    año_pcr= int(input("Año: "))
    mes_pcr= int(input("Mes: "))
    dia_pcr= int(input("Dia: "))
    
    in_fecha_correcta= False
    if año_pcr>0:
        if mes_pcr>0 and mes_pcr<=12:
            maximo_dias=31
            if mes_pcr==1 or mes_pcr==3 or mes_pcr==5 or mes_pcr==7 or mes_pcr==8 or mes_pcr==10 or mes_pcr==12:
                maximo_dias=30
            else:
                if mes_pcr==2:
                    if año_pcr%4==0:
                        if año_pcr%400==0:
                        #si es bisiesto
                            maximo_dias=29
                        else:
                            if año_pcr%100==0:
                            #año no es bisiesto
                                maximo_dias=28
                            else:
                            #no es divisible por 100, es bisiesto
                                maximo_dias=29
                    else:    
                    #año no es bisiesto
                        maximo_dias=28
        #validar el dia
            if dia_pcr>0 and dia_pcr<=maximo_dias:
                print("la fecha es correcta")
                in_fecha_correcta=True
            else:
                print("el dia es incorrecto")
        else:
            print("la fecha es incorrecta")
    else:
        print("el año es incorrecto")
    
    #se verifica si la fecha PCR es correcta
    if in_fecha_correcta:
        #las dos fechas son correctas
        if mes_nac < mes_pcr:
            edad=año_pcr-año_nac
        else:
            if mes_nac > mes_pcr:
                edad=año_pcr-año_nac-1
            else:
                if dia_nac <= dia_pcr:
                    edad= año_pcr - año_nac
                else:
                    edad= año_pcr - año_nac -1    
        print("La edad de la persona es", edad, "años")
    else:
        #la fecha es incorrecta
        print("Debes volver a iniciar el programa")    
else:
    #la fecha es incorrecta
    print("Debes volver a iniciar el programa")
    










