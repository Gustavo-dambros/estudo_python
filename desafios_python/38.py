#compara dois valores e diz quem é maior, ou se são iguais

n1 = int(input('gidite o valor 1 '))
n2 = int(input('digite o valor 2 '))

if n1>n2:
    print('\033[0;32m o valor {}, é maior que o valor {} \033[m'.format(n1,n2))
elif n2>n1:
    print('\033[0;36m o valor {}, é maior que o calor {} \033[m'.format(n2,n1))
else:
    print('\033[0;33m os valores são iguais \033[m')