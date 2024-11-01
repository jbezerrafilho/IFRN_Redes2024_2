conta = int(input('Qual o valor da conta? '))
pago =int(input('Quanto o cliente pagou? '))
troco = pago - conta
troco_variavel = troco

#Calculando quantas cédulas e moeda de cada denominação
cedula100 = troco_variavel // 100
troco_variavel = troco_variavel - (cedula100 * 100)

cedula50 = troco_variavel // 50
troco_variavel = troco_variavel - (cedula50 * 50)

cedula20 = troco_variavel // 20
troco_variavel = troco_variavel - (cedula20 * 20)

cedula10 = troco_variavel // 10
troco_variavel = troco_variavel - (cedula10 * 10)

cedula5 = troco_variavel // 5
troco_variavel = troco_variavel - (cedula5 * 5)

cedula2 = troco_variavel // 2
troco_variavel = troco_variavel - (cedula2 * 2)

moeda1 = troco_variavel

print("Troco: ", troco)
print("Cédula R$ 100:", cedula100)
print("Cédula R$ 50: ", cedula50)
print("Cédula R$ 20: ", cedula20)
print("Cédula R$ 10: ", cedula10)
print("Cédula R$ 5:  ", cedula5)
print("Cédula R$ 2:  ", cedula2)
print("Moeda  R$ 1:  ", moeda1)
