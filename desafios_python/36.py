#emprestimo, pega o valor da casa e o salario, pergunta em quantos anos vai ser se a prestação mensal for maior q 30% do salarios, nega

casa=float(input('qual valor da casa? R$'))
salarios = float(input('qual seu salario?'))

anos=int(input('em quantos anos voce vai pagar?'))*12

prestacao = casa/anos

if prestacao >salarios*0.3:
    print('\033[0;31m emprestimo foi negado\033[m')
else:
    print('\033[0;32m Seu emprestimo foi aceito\033[m')
    