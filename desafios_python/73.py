#voce digita um numero de 0 a 10 e o computador retorna ele em extenso

nExtenso= 'zero', 'um', 'dois', ' tres', ' quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'

continuar='s'
while continuar=='s':


    n=int(input('digite um numero entre 0 e 10'))

    if n>11 or 0>n:
        print("numero fora da sequencia  pedida porfavor digite um numero entre 0 e 10")
        break
    else:
        print(nExtenso[n])
    continuar=input("deseja continuar? s ou n").lower()
print('programa encerrado')
