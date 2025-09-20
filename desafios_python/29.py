#verifica a velocidade e diz se ta mt rapido

velocidade = int(input('qual a velociadde do seu carro? '))
multa=0
if velocidade>80:
    print('voce ta acima a velocidade')
    multa=(velocidade-80)*7
    print('voce esta acima da velocidade, deve pagar R${} de multa'.format(multa))
else:
    print('Muito bem mantenha-se seguro')
