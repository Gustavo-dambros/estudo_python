#contagem regressiva de 10 a 0
from time import sleep
print('\033[4;46m Inicio contagem fogos de artificio \033[m')

n =10

for n in range (10,-1 , -1):
    sleep(1)
    print(n)
print('\033[3;31m BOOM EXPLOSÃO \033[m')
