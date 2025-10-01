#tabuada de um número usando laço

tabuada = int(input('Digite um número para ver a tabuada dele'))

n=0
resultado=0
for n in range (0,10):
    n=n+1
    resultado=tabuada*n
    print('{} x {} = {}'.format(tabuada,n,resultado))

print('essa é a tabuada do número {}'.format(tabuada))
