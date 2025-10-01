#analise completa de cadastro

M=0
H=0

for c in range (1,4):
    print('-----Cadastro individuo {}-----'.format(c))
    nome=input('digite seu nome')
    idade=int(input('qual sua idade'))
    sexo=input('qual seu sexo [f/m]').upper()

    if sexo==('F'):
    
     M=M+1
    elif sexo == ('M'):
        
        H=H+1
    else:
        print('Valor incorrwto')

media=idade/3

print('foram atendidos {} homens, {} Mulheres, e a media de idade da visita foi {} anos '.format(H,M,media))
