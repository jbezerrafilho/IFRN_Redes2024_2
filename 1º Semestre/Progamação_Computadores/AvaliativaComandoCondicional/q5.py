# Calculando o dia Juliano

print('Calendário Juliano.')
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
dia_juliano = 0
data_valida = False

#Validando a data
if  mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 31:
        print('Dia válido')
    else:
        print('Dia inválido')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        print('Dia válido')   
    else:
        print('Dia inválido')
elif mes == 2:
    if dia >= 1 and (dia <= 28 or dia <= 29):
        print('Dia válido')
    else:
        print('Dia inválido')
else: 
    print('Data inválida')

# Calculando o dia Juliano
if data_valida:
    pass

# Falta concluir o código....