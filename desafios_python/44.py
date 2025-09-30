#gerenciados de pagamentos

conta = float(input('Qual valor da sua compra?'))
total=0
pagamento = int(input('qual tipo de pagamento? \n [1]A vista \n [2]A vista no cartão \n [3] 2x no cartão \n[4] 3x ou mais no cartão'))

if pagamento ==  1:
    total = conta - (conta*0.1)
elif pagamento == 2:
    total = conta - (conta*0.05)
elif pagamento == 3:
    total = conta
elif pagamento == 4:
    total = conta + (conta*0.20)

print( 'o valor final da conta foi {:.2f} reais'.format(total))
