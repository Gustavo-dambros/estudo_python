#pegar so a casa inteira do valor digitado
from math import floor 
valor = float(input('digite um valor quebrado: '))

print('o valor da casa inteira é {:.0f}'.format(valor))


print(' o valor digitado foi {} e  a sua versão areedondada (para baixo) é {}'.format(valor, floor(valor)))