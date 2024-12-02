# Developed by J. Bezerra
# November / 2024
# https://projecteuler.net/problem=14 

num = int(input("Digite um número para ver a sequência de Collatz: "))
n = 1
maior_sequencia = -50
num_maior_sequencia = -50

while n <= num:
    numero = n
    qtd_termos = 1
    while numero != 1:
        print(numero, end=" ")
        if numero % 2 == 0:
            numero = int(numero / 2)
        else:
            numero = 3 * numero + 1
        qtd_termos += 1
        
    print(numero)  
    
    if qtd_termos > maior_sequencia:
        maior_sequencia = qtd_termos
        num_maior_sequencia = n
    n += 1

print(maior_sequencia)
print(num_maior_sequencia)  

