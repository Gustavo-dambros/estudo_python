# import math (importa a biblioteca math toda)
#from math import sqrt (importa apenas a raiz quadrada da biblioteca math  ) ex: from math import sqrt

import math
import random

num= random.randint(1, 20)#gera um numero de 1 a 20

numero = int(input('diigte um valor: '))

raiz = math.sqrt(numero)

print('o valor aleatorio gerado foi {}'.format(num))

print('a raiz quadradda de {} é igual a {}'.format(numero, math.floor(raiz)))