#progressão aritimetica
termo1=int(input('digite o primeiro termo '))
razao=int(input('digite a razão de progressão '))
decimo = termo1 + (10-1) * razao
for c in range (termo1,decimo,razao):
    termo1=termo1+razao
    print('{}'.format(termo1))
    