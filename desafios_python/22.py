#make a code to list, the name of a people with all caracter in upper and lower, how much letter have in the name and how much letter have the first name

nome = input('digite seu nome completo ').strip()

print('seu nome completo é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))

print('seu nome contem {} letras'.format(len(nome) - nome.count(' ')))#count the white spaces 

nome.split()
dividida = nome.split()

print('seu primeiro nome é {}'.format(len(dividida[0]) ))
