#descobrir se um numero é primo

n = int(input('digite um numero:'))
c=0
contador=0
for c in range(0,n):
    c=c+1
    if n%c==0:
        print('\033[0;32m{}\033[m'.format(c))
        contador=contador+1
    else:
        print('\033[0;31m{}\033[m'.format(c))
    
if contador>2:
    print('numero não primo')
else:
    print('numero primo') 
    