dia=int(input("digita el dia:"))
mes=int(input("digita el mes:"))
año=int(input("digita el año:"))

if año>0:
    if mes>0 and mes<=12:
        maximo_dias=31
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
           maximo_dias=30
        else:
            if mes==2:
                if año%4==0:
                    if año%400==0:
                        #si es bisiesto
                        maximo_dias=29
                    else:
                        if año%100==0:
                            #año no es bisiesto
                            maximo_dias=28
                        else:
                            #no es divisible por 100, es bisiesto
                            maximo_dias=29
                else:    
                    #año no es bisiesto
                        maximo_dias=28
        #validar el dia
        if dia>0 and dia<=maximo_dias:
            print("la fecha es correcta")
        else:
            print("el dia es incorrecto")
    else:
        print("la fecha es incorrecta")
else:
    print("el año es incorrecto")