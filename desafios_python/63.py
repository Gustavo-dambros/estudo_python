#sequencia de fibonacci

qnt=int(input("quantos termos voce ddeseja mostrar? "))
c=0
valor=0
valor2=1

while c!=qnt:
    valor3=valor+valor2
    print("->{}".format(valor3))
    valor=valor2
    valor2=valor3
    c += 1
    