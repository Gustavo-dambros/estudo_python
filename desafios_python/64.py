#tratando varios valores, voce deve colocar eles, até colocar 999 quando colocar ele para

valor=int(input("digite um valor, ou 999 para parar"))
banco=0

while valor != 999:
    banco += valor
    valor=int(input("digite um valor, ou 999 para parar"))
    
print(banco)
