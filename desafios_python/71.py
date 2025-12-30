#lista de compras
caro=0
barato=' '
mais_barato=' '
soma=0
cont=0
while True:
    
    name=input("qual nome do produto que você deseja comprar?")
    preco=int(input("quanto custa esse produto?"))
    cont = cont + 1
    if cont ==1:
        mais_barato=preco

    else:
        if mais_barato>preco:
            barato=name
    conti=input('deseja continuar? (s ou n)').lower()

   

    soma = soma + preco

    if preco>1000:
        caro=caro+1

    if conti =="n":
        break
    
    
print(f"o valor da compra foi {soma} reais \n {caro} produtos custavam mais que 1000 reais \n o produto mais barato foi {barato}")
