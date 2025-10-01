#analisa se a pessoa é d emaior ou não
from datetime import date
data=date.today().year
for c in range (0,7):
    n=int(input('digite o ano de nascimento da pessoa {} '.format(c)))
    if data-n>=18:
        print('maior de idade')
    else:
        print('de menor')
