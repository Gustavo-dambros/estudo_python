#progressao aritmetica usando while versao 2.0

P_termo=int(input("Digite o primeiro termo"))
progressao=int(input("digite a progressão aritmetica"))
c=0
cont=10
cont_extra=0



while cont!=c:
        print("{}->".format(P_termo), end='')
        P_termo=P_termo + progressao
        c=c+1

      

continuar=input("Deseja continuar? S/N ").lower()

if continuar=="s":
    cont_extra=int(input("Quantos termos a mais voce deseja ver?"))
    cont += cont_extra
    
    while cont!=c:
        print("{}->".format(P_termo), end='')
        P_termo=P_termo + progressao
        c=c+1

elif continuar=="n":
    print("bom mesmo")

else:
    print("digita certo porra")


