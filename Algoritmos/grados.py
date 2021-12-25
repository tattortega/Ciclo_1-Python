print("\nDigita la fecha de nacimiento del paciente")
dia_nac=int(input("Dia: "))
mes_nac=int(input("Mes: "))
año_nac=int(input("Año: "))

#se valida que la fecha de nacimiento es correcta
fecha_correcta= False
while fecha_correcta:
    if año_nac>0:
        if mes_nac>0 and mes_nac<=12:
            maximo_dias=31
            if mes_nac==1 or mes_nac==3 or mes_nac==5 or mes_nac==7 or mes_nac==8 or mes_nac==10 or mes_nac==12:
               maximo_dias=30
            else:
                if mes_nac==2:
                    if año_nac%4==0:
                        if año_nac%400==0:                        
                            maximo_dias=29
                        else:
                            if año_nac%100==0:                           
                                maximo_dias=28
                            else:                            
                                maximo_dias=29
                    else:                        
                        maximo_dias=28        
            if dia_nac>0 and dia_nac<=maximo_dias:           
                fecha_correcta=True
            else:
                print("la fecha de nacimiento es incorrecta")
        else:
            print("la fecha de nacimiento es incorrecta")
    else:
        print("la fecha de nacimiento es incorrecta")
    