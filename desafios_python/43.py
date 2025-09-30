#calculadora de IMC

peso = float(input('qual seu peso em KG?'))
altura = float(input('qual sua altura em metros?'))

imc = peso/(altura**2)

if imc<18.5:
    print('voce esta abaixo do peso ')
elif 18.5<=imc>25:
    print('peso ideal')
elif 25<=imc>30:
    print('sobre peso')
else:
    print('obesidade')
