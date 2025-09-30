#recebe 3 valores, e diz q tipo de triangulo sera formado

n1 = float(input('digite um valor '))
n2 = float(input('digite o segundo valor '))
n3 = float(input('digite o terceito valor '))

if n1==n2 and n2==n3 and n3==n1:
    print('com esses valores pode ser feito um triangulo equilatero')
elif n1!=n2 and n2!=n3 and n3!=n1:
    print('com valores diferentes pode fazer um triangulo escaleno')
else:
    print(' pode ser feito um triangulo isosceles')