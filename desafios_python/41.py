#recebe a idade de um atleta e classifica ele
from datetime import date
idade = int(input('qual seu ano de nascimento?'))
idade =date.today().year-idade
if 9>=idade:
    print('voce é mirim')
elif 14>idade>=10:
    print('você é infantil')
elif 19>idade>=15:
    print('você é junior')
elif 25>idade>16:
    print('voce é senior')
else:
    print('você é master')
