#soma todos os valores multiplos de 3 e impares entre 0 e 500

multi=0
soma =0
cont =0
for multi in range(0, 501):
   
    if multi % 2 ==1 and multi%3==0:
       cont=cont+1 
       soma= multi + soma

print(soma)
print('foram contados {} numeros'.format(cont))