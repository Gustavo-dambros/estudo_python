#analisa a frase e diz, quantas letras R tem, onde ela aparece pela primeira vez e onde ela aparece pela ultima

frase = input('digite uma frase:').strip()
frase = frase.lower()
print('a letra R aparece {} vezes'.format(frase.count('r', 0,)))
print('ela aparece pela primeira vez na posição {}'.format(frase.find('r')+1))
print('a ultima letra R aparece na posição {}'.format(frase.rfind('r')+1))