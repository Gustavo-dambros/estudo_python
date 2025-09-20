#5% de desconto no produto

valor = float(input('digite o valor do produto: '))

porcentagem = valor*5/100
desconto = valor - porcentagem

print(' o valor inicial do produto era {} com desconto ele passa a custar {}'.format(valor,desconto))
