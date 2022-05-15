from math import sin,cos,tan, radians
a = float(input('Digite o valor de um angulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O valor de Seno é {:.2f}, cosseno {:.2f} e tangente {:.2f}. ' .format(seno, cosseno, tangente))

