#lista de valores

produtos = ('lapis', 1.10, 'caneta', 2.50, 'panela', 100.99)


print('_-' *30)
for pos in range(0, len(produtos)):
    if pos % 2 ==0:
        print (f'{produtos [pos]:-<30}', end=' ' )
    else:
        print(f'R$ {produtos [pos]}')