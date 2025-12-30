#oque são tuplas em python?

lanche='hamburguer','pizza','pudim','comida','pao de queijo'

print(lanche)
n=3
#for comida in lanche:
#    print(f'eu comi {comida}')

#print (f'as 3 primeiras comidas q eu comi foram{lanche[0:n]}')
#print(len(lanche))#quantos elementos tem na tupla

#for cont in range(0, len(lanche)):
#    print(f'{lanche[cont]} na posição {cont}')

#coloca em ordem alfabetica
#print(sorted(lanche))

a=1,3,4,5,1,3,
b=2,3,4,5,1,0

c=a+b
#print(sorted(c))

#mostra quantos 1 tem
print(c.count(1))

#mostra posição do 0
print(c.index(0))
print(len(c))