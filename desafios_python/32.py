#analisa o ano e diz se ele é bissexto
from datetime import date
data = int(input('qual o ano vc quer analisar? se quiser esse ano digite 0: '))

if data==0:
    data=date.today().year 
if data % 4 == 0  :
        print('o ano {} é bissexto'.format(data))
else:
        print('o ano de {} não é bissexto'.format(data))