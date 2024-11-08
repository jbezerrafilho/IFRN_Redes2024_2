a = int(input("Digite o coeficiente a para a equação de 2º grau: "))
delta = 0

if a != 0:
    b = int(input("Digite o coeficiente b para a equacao de 2º grau: "))
    c = int(input("Digite o coeficiente c para a equacao de 2º grau: "))
    delta = b ** 2 - 4*a*c
    if delta < 0:
        print("Equação sem raízes reais!")
    else:
        x1 = (- b + delta ** (1/2)) / ( 2 * a )
        x2 = (- b - delta ** (1/2)) / ( 2 * a )
        print("O valor de x1 é:", x1)
        print("O valor de x2 é:", x2)
else:
    print("O coeficiente 'a' não pode ser 0!")
