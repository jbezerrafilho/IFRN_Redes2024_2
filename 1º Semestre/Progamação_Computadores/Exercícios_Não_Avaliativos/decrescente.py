numero = int(input("Digite um numero de 04 dígitos))

#Capturando o número mais significativo
a = numero // 1000 
numero = numero % 1000

b = numero // 100
numero = numero % 100

c = numero // 10
numero = numero % 10
