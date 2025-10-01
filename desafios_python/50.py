#lê 6 valores, se for par soma se ffor impar desconsidera
cont=0
soma=0
for cont in range (0,6):
    val=int(input('digite um valor'))
    if val%2==0:
        soma=soma+val
        cont=cont+1
    else:
        cont=cont+1
print('a soma dos valores pares foi {}'.format(soma))