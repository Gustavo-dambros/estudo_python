#analisa 3 segmentos e diz se eles podem formar um triangulo

seg1 = float(input('digite a mediada do primeiro segmento: '))
seg2 = float(input('digite a medidda do segundo segmento:'))
seg3 = float(input('ddigite o valor do terceiro segmento: '))

if seg1 < seg2 +seg3 and seg2 < seg1+seg3 and seg3<seg1+seg2:
    print('podem formar um triangulo')
else:
    print('nao podem formar um triangulo')