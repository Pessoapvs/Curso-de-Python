'''co=float(input('Qual o comprimento do cateto oposto: '))
ca=float(input('Qual o comprimento do cateto adjacente: '))
h=(co ** 2 + ca **2)**(1/2)
print("A hipótenusa vai medir {:.2f}".format(h))'''

import math
co=float(input('Qual o comprimento do cateto oposto: '))
ca=float(input('Qual o comprimento do cateto adjacente: '))
hi=math.hypot(co, ca)
print("A hipótenusa vai medir {:.2f}".format(hi))