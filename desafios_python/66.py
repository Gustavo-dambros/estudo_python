#digite valores, quando digitar 999 para e resulta a soma

print("Digite qualquer numero, para parar digite 999")
n = 0
s = 0

while True:
    n = int(input("Digite um valor"))
    
    if n==999:
        break
    s += n
print(f"a soma foi{s}")
