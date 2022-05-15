from math import hypot
oposto = float(input('Qual a medidada do cateto oposto? '))
adjacente = float(input('Qual a medida do cateto adjacente?'))
hipotenusa = hypot(oposto, adjacente)
print('O valor da hipotenusa é igual a {:.2f} ! '. format(hipotenusa))
