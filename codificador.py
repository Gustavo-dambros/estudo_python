#teste de codificador
import random
import string
n=0
frase=input('digite uma frase')
nf=len(frase)
a=random.choice(string.ascii_letters).lower()
b=random.choice(string.ascii_letters).lower()
for n in range (0,nf):
    frase.replace('b',a)
