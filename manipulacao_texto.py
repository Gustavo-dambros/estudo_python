#manipulação de texto
#se usar o r ou l ele começa a fazer a ação pela direção
frase = input('digite uma frase: ')
p9 = frase[5]


print (frase[7])
print (frase[2:4])  #pega a posição 2 ate a 4, mas exclui a 4
print (frase[2:9:1]) #conta do dois ao 9 pulando de 1 em 1
#[:5] comeca do inicio at eo 5 
print(p9)
print(len(frase)) #conta caracter
print (frase.count('a', 0, 10)) #conta quantas vezes o a aparece do 0 ao 10
print (frase.find('deo')) #acha onde começa o deo/se retornar -1, valor nao encontrado
print('curso' in frase)

#como editar

print(frase.replace('a','b'))#substitiui o primeiro pelo segundo
print(frase.upper())#deixa tudo maiusculo   LOWER() faz o mesmo
print(frase.capitalize()) #deixa tudo em minusculo, so o primeiro caracter em maisuculo
print(frase.title())#deixa todas as palavras com a primeiro letra maiuscula

print(frase.strip())#retira os espaços inuteis no começo ou final do texto se usar rstrip remove so da direita msm coisa p esquerda

dividida = frase.split()#transofrma a frase em uma lista separada por espaços
print( dividida [2] [2])#pega o elemento 2 da lista e o caracter na posição 2
'-'.join(frase)#dps de usa o split ne, voce junta os elementos da lista separados pleo oq ta entre aspas