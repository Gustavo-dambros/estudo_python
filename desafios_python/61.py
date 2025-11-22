#progressao aritmetica usando while

P_termo=int(input("Digite o primeiro termo"))
progressao=int(input("digite a progressão aritmetica"))
c=0

while 10!=c:
    print("{}->".format(P_termo), end='')
    P_termo=P_termo + progressao
    c=c+1
print("FIM")
