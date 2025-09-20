#lista aleatoria
import random 
al1 = input('digite o nome do aluno 1: ')
al2 = input('digite o nome do aluno 2')
al3 = input('digite o nome do aluno 3')

lista = [al1, al2, al3]

random.shuffle(lista)

print('a ordem de apresentação sera ')
print(lista)