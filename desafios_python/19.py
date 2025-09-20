#sortear um aluno    Listsa
import random

al1 = input('digite um aluno: ')
al2 = input('digite o 2 aluno:')
al3 = input('digite o 3 aluno:' )
al4 = input('digite o 4 aluno:')

lista = [al1, al2, al3, al4 ]

sorteio = random.choice(lista)

print(' o aluno escolhido foi {}'.format(sorteio))