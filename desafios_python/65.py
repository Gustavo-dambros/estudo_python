#coloca varios valores, calcula a media, o maior o menor e quantos numeros foram digitados

flag="s"
c=0
soma=0
maior=0
menor=0
media=0
while flag=="s":
    n=int(input("Digite o valor: "))
    
    if n<menor:
        menor = n
    if n > maior:
        maior=n
    flag=input("voce deseja continuar?").lower()
    c += 1
    soma += n

media = soma/c

print("voce digitou {} numeros a media deles foi {} \n o menor dele foi {} e o maior foi {}".format(c , media, menor ,maior))
