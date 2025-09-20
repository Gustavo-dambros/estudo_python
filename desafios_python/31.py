#analisa a distancia da viagem, ate 200 km cobra R$0,50 por km, se for mais q 200km
#cobra R$0,25 por km

distancia = int(input('qual a distancia da sua viagem? '))

if distancia<200:
    preco = distancia*0.5
    print('sua corrida eu R${:.2f}'.format(preco))
else:
    preco=distancia*0.25
    print ("sua corrida deu R${:.2f}".format(preco))