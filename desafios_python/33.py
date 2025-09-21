#recebe 3 valores e diz qual é menor e qual o maior

st=int(input('digite um valor'))
nd=int(input('digite o seguno valor'))
rd=int(input('digite o terceito valor'))

menor=st
if nd<st and nd<rd:
    menor=nd
if rd<st and rd<nd:
    menor=rd

maior=rd
if st>nd and st>rd:
        maior=st
if nd>st and nd>rd:
        maior=nd

print('o menor numero é {}\ne o maior numero é {}'.format(menor,maior))