#Gera 5 valores aleatorios, em uma tupla e mostra o maior, e menor

from random import randint
numeros=(randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20), )

for n in numeros:
    print(f"{n} ")
print(f"o maior valor sorteado foi {max(numeros)}/n")
print(f"e o menor sorteado foi {min(numeros)}")
