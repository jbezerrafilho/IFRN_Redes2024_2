# Developed by J.Bezerra
# Novembro de 2024
try:
    print()
    print('Calendário Juliano.')
    dia = int(input('Informe o dia: '))
    mes = int(input('Informe o mês: '))
    ano = int(input('Informe o ano: '))
    dia_juliano = 0
    data_valida = False
    eh_bissexto = False
    ano_valido = True

    # Validando se o ano é válido e bissexto
    if ano < 0:
        ano_valido = False
        print('Ano inválido!\n')
    elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        eh_bissexto = True


    if ano_valido:
        # Validando dia do mês
        if  mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia >= 1 and dia <= 31:
                data_valida = True
            else:
                print('Dia inválido')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia >= 1 and dia <= 30:
                data_valida = True   
            else:
                print('Dia inválido')
        elif mes == 2 and eh_bissexto:
            if dia >= 1 and dia <= 29:
                data_valida = True
        elif mes == 2: 
            if dia >= 1 and dia <= 28:
                data_valida = True
            else:
                print('Dia inválido')
        else: 
            print('Data inválida')
        

    # Calculando o dia Juliano
    if data_valida or eh_bissexto:
        if mes == 1:
            dia_juliano = dia
        if mes == 2 :
            dia_juliano = 31 + dia

    if data_valida and eh_bissexto:
        if mes == 3:
            dia_juliano = 60 + dia
        if mes == 4:
            dia_juliano = 91 + dia
        if mes == 5:
            dia_juliano = 121 + dia
        if mes == 6:
            dia_juliano = 152 + dia
        if mes == 7:
            dia_juliano = 182 + dia
        if mes == 8: 
            dia_juliano = 213 + dia
        if mes == 9:
            dia_juliano = 244 + dia
        if mes == 10:
            dia_juliano = 274 + dia
        if mes == 11:
            dia_juliano = 305 + dia
        if mes == 12:
            dia_juliano = 335 + dia

    if data_valida and not eh_bissexto:
        if mes == 3:
            dia_juliano = 59 + dia
        if mes == 4:
            dia_juliano = 90 + dia
        if mes == 5:
            dia_juliano = 120 + dia
        if mes == 6:
            dia_juliano = 151 + dia
        if mes == 7:
            dia_juliano = 181 + dia
        if mes == 8: 
            dia_juliano = 212 + dia
        if mes == 9:
            dia_juliano = 243 + dia
        if mes == 10:
            dia_juliano = 273 + dia
        if mes == 11:
            dia_juliano = 304 + dia
        if mes == 12:
            dia_juliano = 334 + dia
            
    print(f'Seu dia juliano é {dia_juliano}.') if data_valida else None

except ValueError as e:
    print(e)
    print('Digite um número válido!')