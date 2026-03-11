#le 4 valores, fala quantas vezes aparecceu o numero 9 qual a primeria posição com 3 e quais são valores pares

numeros=(int(input("Diite um numero")), int(input("Diite mais um numero")), int(input("Diite outro numero")), int(input("Diite um ultimo numero")), )

print(f"você digitou os valores{numeros}")
print(f"o número 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"a primeira vez que o numero 3 aparece é na posição {numeros.index(3)+1}")
else:
    print("o valor 3 nao foi declarado")
print("os numeros pares são:")
for n in numeros:
    if n % 2 ==0:
        print(n)
