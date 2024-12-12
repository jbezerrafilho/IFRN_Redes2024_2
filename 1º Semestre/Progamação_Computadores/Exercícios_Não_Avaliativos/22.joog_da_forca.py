sorteada = 'VISAO'
atual = "_" * len(sorteada)

while atual != sorteada:
    letra = input('Digite uma letra: ')
    # A variável 'nova' foi criada porque não podemos atualizar atual 
    # Lmebre-se que String é invariável
    nova = ''

    for posicao in range(len(sorteada)):
        if sorteada[posicao] == letra.upper():
            nova = nova + sorteada[posicao]
        else:
            nova = nova + atual[posicao]
    print(nova)
    atual = nova