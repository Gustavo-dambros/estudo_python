#pedra papel tesoura

import random

jogador = int(input('escolha:\n[0] Pedra \n [1] Papel  \n [2]Tesoura \n'))
maquina = random.randint(0,2)

if jogador ==0 and maquina ==1:
    print(' voce escolheu pedra e a maquina papel, a maquina venceu')

elif jogador ==0 and maquina ==2:
    print(' voce escolheu pedra, a maquina escolheu tesoura, voce perdeu')
elif jogador ==1 and maquina ==0:
    print('voce jogou papel, a maquina jogo pedra, voce venceu')
elif jogador ==1 and maquina ==2:
    print('voce jogou tesoura a maquina jogou papel, voce perdeu')
elif jogador ==2 and maquina ==0:
    print('voce jogou tesoura a maquina jogou pedra, voce perdeu')
elif jogador ==2 and maquina ==1:
    print('voce jogou tesoura, a maquina jogou papel, voce venceu ')
elif jogador == maquina:
    print('EMPATE')
else:
    print('\033[0;31m Jogada nao valida \033[m')


#explicação do professor
#if maquina ==0:
#if jogador ==0:
# print(empate)

#if dentro de if