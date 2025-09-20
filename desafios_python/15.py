#calcule o aliguel do carro, 60 por dia e 0.25 por km rodado

dias = int(input('quantos dias o carro foi alugado?'))
km = float(input('quantos km voce rodou no carro?'))

diasP = dias*60
kmP = km*0.15

total=kmP+diasP

print('o total a ser pago foi de {}'.format(total))