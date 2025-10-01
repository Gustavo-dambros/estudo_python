#identifica se o numero é um palindromo

frase = input('digite uma frase: ').replace(' ', '').upper()
inverso=''
for letra in range (len(frase)-1,-1,-1 ):
    inverso += frase[letra]
if inverso==frase:
    print('é um palindromo')
else:
    print('nao é um palindromo')
