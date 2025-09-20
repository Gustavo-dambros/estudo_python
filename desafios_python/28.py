# o computaddor pena em um numero e voce tenta adivinhar
from time import sleep
import random
CPU_n=random.randint(0,5)
print('-=-'*30)
Player_n = int(input('pensei em um numero de 0 a 5, tente aivinhar:'))
print('pensando..')
sleep(1.5)

if CPU_n ==Player_n:
    print('VocÊ acertou PARABENS')
else:
    print('ERROU eu ganhei pensei no numero {}'.format(CPU_n))

print('fim do jogo')