#analisa o maior e menor valor de uma lista
menor=1
maior=1
for c in range (1,6):
    n=int(input('digite um valor: '))
    if n>maior:
        maior=n
    if n<=menor:
        menor=n
print(' o menor valor foi {}, e o maior foi{}'.format(menor,maior))
