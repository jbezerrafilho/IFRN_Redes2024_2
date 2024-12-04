num = int((input('Digite um número para ver quantos primos existe entre 2 e ele: ')))
qtd_primos = 0

i = 0
while i <= num:    
    j = 1
    ndiv = 0
    while j <= i:
        if i % j == 0:
            ndiv += 1
        j += 1
    if ndiv == 2:
        qtd_primos += 1
    i += 1
print(qtd_primos)
