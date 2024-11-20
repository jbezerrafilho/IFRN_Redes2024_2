try:
    print()
    print('Organização didática do IFRN')
    print('Seção II')
    print('Cálculo de média em Disciplinas!')
    print()

    msg = 'Digite a nota: '
    situacao = ''
    n1 = float(input(msg))
    n2 = float(input(msg))
    naf = 0 # nota de avaliação final, caso necessário

    # Média da Disciplina
    md = (2 * n1 + 3 * n2) / 5
    print('A média da disciplina foi: ', md)
    if md >= 60:
        situacao = 'Aprovado'
        print(situacao)

    elif 20 <= md < 60:
        print('Em prova final')
        naf = float(input(msg))

        #Três formas de calcular a média final
        #A mais vantajosa será considerada
        mfd = (md + naf) / 2
        mfd1 = (2 * naf + 3 * n2) / 5
        mfd2 = (2 * n1 + 3 * naf) / 5
        if mfd >= 60 or mfd1 >= 60 or mfd2 >= 60:
            situacao = 'Aprovado'
            print('Aprovado')
        else:
            situacao = 'Reprovado'
            print(situacao)
    else:
        situacao = 'Reprovado'
        print(situacao)

    #Se o estudante não for reprovado por falta 
    #E tiver média superior a 20, poderá fazer avaliação final

except ValueError as e:
    print(e)
    print('Digite uma nota válida!')