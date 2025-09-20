valor1 =int(input('digie um numeoro:'))
valor2= int(input('digite outro numero:'))


soma =valor1 + valor2
subtracao = valor1 - valor2
divisao = valor1/valor2
multiplicacao = valor1 * valor2
potencia = valor1 ** valor2
divisao_Semresto = valor1//valor2

print('voce digitou {:=^2} e {:=^2}'.format(valor1,valor2))
print('a soma é {} a subtração é {} a divisão é {} a multiplicação é {} a potencia é {} e a divisao sem resto é {}'.format(soma,subtracao,divisao,multiplicacao,potencia, divisao_Semresto))
#comentario de uma linha, oque vai primeiro é potencia, as div e multiplicações dai faz as somas e subtrações 