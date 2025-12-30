#caaixa eletronocio que lÊ cedulas 

c50=0
c20=0
c10=0
c1=0

print("=" * 30)
print("Caixa eletronico")
print("=" * 30)

valor = int(input("quantos reais voce deseja sacar?"))
inteiro=valor 

while True:
    while inteiro >= 50:
        inteiro = inteiro - 50
        c50 += 1
    if inteiro < 50:
        while inteiro >= 20:
            inteiro = inteiro - 20
            c20 += 1
    if inteiro < 20:
        while inteiro >=10:
            inteiro = inteiro -10
            c10 +=1
    if inteiro <10:
        while inteiro >=1:
            inteiro = inteiro -1
            c1 +=1

    if inteiro ==0:
        break

print(f"foram usadas {c50} cedulas de 50 reais e {c20} de 20 reais, {c10} de 10 reais e {c1} de um real" )

