#converte um numero de decimal para binario, octal e hexadecimal

n=int(input('digite um numero inteiro:'))

tipo = int(input('escolha qual tipo voce quer fazer:\n  1 para binario \n 2 para octal \n 3 para hexadecimal \n'))

if tipo ==1:
    print('\n \033[4;36m o numero {} em binario é {} \033[m'.format(n,bin(n)[2:]))
elif tipo==2:
    print('\n  \033[4;36m o numero{} em ocatl é {} \033[m'.format(n, oct(n)[2:]))
else:
    print('\n \033[4;36m o numero {} em hexadecimal é {} \033[m '.format(n, hex(n)[2:]))