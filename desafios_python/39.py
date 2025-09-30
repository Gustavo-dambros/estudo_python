#lê o ano de nascimento do jovem, diz se ele ja deve se alistar ou quanto tempo falta pro alistamento

from datetime import date

nasc = int(input('Qual ano você nasceu?'))

data=date.today().year
 
tempo = data-nasc
if tempo>18:
    print('já passou o tempo de se alistar soldado')
elif tempo==18:
    print('hora de se alistar solado')
else:
    print('ainda não é seu momento jovem, faltam {} anos para seu alistamento obrigatorio'.format(18-tempo))
