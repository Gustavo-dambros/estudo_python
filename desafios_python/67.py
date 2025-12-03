#Mostra a tabuada do valor digitado pelo usuario, se o valor for negativo interrompe o programa
n=0
t=0
while True:

    n = int(input("digite um valor para saber a tabuada dele"))

    if 0>n:
        break
    for t in range (0,11):
        print(f"{n} X {t} = {n*t}")
        

print("valores negativos nao sao suportador")