#calculo de faotrial

n = int(input('digite o valor que voce quer calcular o fatorial '))
contagem = n
f=1
while contagem > 1:
   f*=contagem
   contagem=contagem-1
print(' o fatorial é {}'.format(f))
