import random

try:
    numero_sorteado = random.randint(1, 100)
    
    # Definindo início do intervalo
    inicio = 1
    fim = 100

    #Tentativa 1
    msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
    tentativa = int(input(msg))
    if tentativa == numero_sorteado:
        print(f'Você acertou o número secreto {numero_sorteado}!')
    elif tentativa < numero_sorteado:
        inicio = tentativa + 1
        fim = 100
    else:
        inicio = 0
        fim = tentativa - 1

    #Tentativa 2
    msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
    tentativa = int(input(msg))
    if tentativa == numero_sorteado:
        print(f'Você acertou o número secreto {numero_sorteado}!')
    elif tentativa < numero_sorteado:
        inicio = tentativa + 1
        fim = 100
    else:
        inicio = 0
        fim = tentativa - 1

    #Tentativa 3    
    msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
    tentativa = int(input(msg))
    if tentativa == numero_sorteado:
        print(f'Você acertou o número secreto {numero_sorteado}!')
    elif tentativa < numero_sorteado:
        inicio = tentativa + 1
        fim = 100
    else:
        inicio = 0
        fim = tentativa - 1
    
    #Tentativa 4    
    msg = f'Qual o número sorteado no intervalo de {inicio} a {fim}? '
    tentativa = int(input(msg))
    if tentativa == numero_sorteado:
        print(f'Você acertou o número secreto {numero_sorteado}!')
    elif tentativa < numero_sorteado:
        inicio = tentativa + 1
        fim = 100
    else:
        inicio = 0
        fim = tentativa - 1
    print('Que pena, Game Over!!')
except ValueError as e:
    print(e)
    print('Digite um número válido!')