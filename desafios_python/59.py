#calculadora interativa

print('escolha dois valore para começar o programa')
n1=int(input('digite o valor 1 '))
n2=int(input('digite o valor 2 '))
resultado=0
opc=0
while opc !=5:

    print('[1] somar\n[2] subtrair\n[3] dividir\n[4] multiplicar')
    opc=int(input(''))


    if opc==1:
        resultado=n1+n2
        print('o resultado da soma é {}'.format(resultado))
    elif opc==2:
        resultado=n1-n2
        print('o resultado da subtração é {}'.format(resultado))
    elif opc==3:
        resultado=n1/n2
     
    elif opc==4:
        resultado=n1*n2
        print('o resultado da multiplicação é  {} '.format(resultado))
print('o resultado da operação foi {}'.format(resultado))
