#seno, cosseno e tang

import math

valor = int(input('digite um angulo:'))

seno =math.sin(math.radians(valor))
cos =math.cos(math.radians(valor))
tan = math.tan(math.radians(valor))


print('o valor do seno de {} é {:.2f} \n o cosseno é {:.2f} \n a tangente é {:.2f}'.format(valor,seno,cos,tan))