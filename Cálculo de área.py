a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
area = a*l
tinta = area/2
print('A area corresponde a {} metros e será necessário {} litros de tinta para efetuar a pintura completa da parede.'
.format(area,tinta))
