# Developed by J. Bezerra
# November / 2024
# https://projecteuler.net/problem=14

num = int(input("Digite um número para ver a sequência de Collatz: "))
print(num)
qtd_termos = 1
contador = 0
maior = 0
n = 0

while contador <= num:
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        print(num)
        qtd_termos += 1
    
    if qtd_termos > maior:
        maior = qtd_termos
    contador += 1
    n = num

print(f"A quantidade de termos para {n} é {qtd_termos}")