d = float(input('Qual a distância de sua viagem? '))
if d <= 200:
    a = d * 0.50
    print('Você está prestes a começãr uma viagem de {:.1f}km !'.format(d))
    print('E o preço da passagem será de R${:.2f}'.format(a))
else:
    b = d * 0.45
    print('Você está prestes a começãr uma viagem de {:.1f}km !'.format(d))
    print('O preço de sua passagem será de R${:.2f}'.format(b))
