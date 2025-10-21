#jogo de adivinhar
import random
tentativas=0
n= random.randint(1,10)
R=int(input('Pensei em um nùmero tente adivinhar qual foi '))
while n!=R:
    R=int(input('você errou tente denovo'))
    tentativas=tentativas + 1
print('parabens, você acertou, eu pensei no numero {} voce só precisou de {} tentativas '.format(n,tentativas))
