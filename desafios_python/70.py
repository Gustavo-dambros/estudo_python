#analise de dados do grupo

h=0
maior=0
m=0
menores=0

while True:
    print('Cadastre uma pessoas:')
    genero=input("qual genero dessa pessoa? (H ou M)").lower()
    idade=int(input('qual a idade dela?'))


    if genero == "m":
        m = m +1

    elif genero == "h":
            h = h +1

    else:
        ("print coloque o valor correto")
        break

    if idade>18:
         maior= maior + 1

    if genero=="m" and idade>20:
         menores = menores + 1
    
    continuar=input("deseja continuar? (s ou n)").lower()
    if continuar=="n":
         break
   

print(f"foram entrevistadas  {m} mulheres, {h} homens, deles {menores} eram mulheres menores de 20 e {maior} eram maiores de idade")
