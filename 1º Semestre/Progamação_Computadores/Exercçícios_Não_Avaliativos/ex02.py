print("Digite um número de três dígitos: ")
num = int(input())

centena = num // 100
num = num - (centena * 100)

dezena = num // 10
num = num - (dezena * 10)

unidade = num

print(unidade, dezena, centena)