#a soma dos catetos é igual a porra da hipotenusa
import math

cateto_adj = float(input('digite o valor do cateto ajascente: '))

cateto_oposto = float(input('digite o valor do cateto oposto: '))

#hipotenusa = math.sqrt (cateto_adj**2 + cateto_oposto**2)
hipotenusa = math.hypot(cateto_adj, cateto_oposto)
print('o valor da hipotenusa vai ser {:.2f}'.format(hipotenusa))