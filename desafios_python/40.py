#media, aluno reporvado ou aprovaod

n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota:  '))

media =(n1+n2)/2

if media>6.90 or media>69:
    print('sua nota foi {} voce esta APROVADO'.format(media))
elif 5>media:
    print('você foi reporvado sua nota foi {}'.format(media))
elif media>5 and media<7:
    print('você esta com a nota {}, cuidado tu ta de recuperação'.format(media))
