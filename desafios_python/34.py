#para salarios maiores de R$1250 aumenta 10% para menores aummenta 15%

salario = float(input('qual seu salrio? em R$ '))

if salario>1250:
    salario=salario+(salario*0.10)
    print('seu salario aumentou 10%, agora ele é {}'.format(salario))
else:
    salario=salario+(salario*0.15)
    print('seu salario aumentou 15%, agora ele é {}'.format(salario))
    