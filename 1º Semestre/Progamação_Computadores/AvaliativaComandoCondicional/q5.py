# Calculando o dia Juliano

print('Calendário Juliano.')
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
dia_juliano = 0
eh_data_valida = False
eh_bissexto = False

#Validando a data
if  mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 31:
        print('Dia válido')
        eh_data_valida = True
    else:
        print('Dia inválido')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        print('Dia válido')
        eh_data_valida = True   
    else:
        print('Dia inválido')
elif mes == 2:
    if dia >= 1 and (dia <= 28 or dia <= 29):
        print('Dia válido')
        eh_data_valida = True
    else:
        print('Dia inválido')
else: 
    print('Data inválida')

# Validando se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        eh_bissexto = True

# Calculando o dia Juliano
if eh_data_valida and eh_bissexto:
    if mes == 12:
        dia_juliano = 335 + dia
    if mes == 11:
        dia_juliano = 305 + dia
    if mes == 10:
        dia_juliano = 274 + dia
    if mes == 9:
        dia_juliano = 244 + dia
    if mes == 8: 
        dia_juliano = 213 + dia
    if mes == 7:
        dia_juliano = 182 + dia
    if mes == 6:
        dia_juliano = 152 + dia
    if mes == 5:
        dia_juliano = 121 + dia
    if mes == 4:
        dia_juliano = 91 + dia
    if mes == 3:
        dia_juliano = 60 + dia
    if mes == 2:
        dia_juliano = 31 + dia
    if mes == 1:
        dia_juliano = dia

    print(dia_juliano)