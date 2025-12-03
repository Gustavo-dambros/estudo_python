#jogo da par ou impar so para se o jogador perde

import random

while True:
    maquina = random.randint(1,10)
    jogador = int(input("escolha um numero"))
    pi=input("voce quer par ou impar?").lower()
    
    s= maquina + jogador

    print(f"O jogador jogou{jogador} e a maquina jogou {maquina} a soma é {s}")

    if pi=="par":
        if s % 2 == 0:
            print("o jogador venceu")
        else:
            print("o jogador perdeu")
            break
    if pi=="impar":
        if s % 2 == 1:
            print("o jogador venceu")
        else:
            print("o jogador perdeu")
            break

print("o jogo acabou")
