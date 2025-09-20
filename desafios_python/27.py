#acha o primeiro e ultimo nome do usuario

nome = input('qual seu nome?').strip()
nome = nome.split()

print('seu primeiro nome é{}'.format(nome[0]))

print('seu último nome é: {}'.format(nome[len(nome)-1]))#quantidade de intens na lista, menos 1 pq a posição começa em 0
