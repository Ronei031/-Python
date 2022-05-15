v = int(input('Qual a velocidade do carro?'))
a = (v-80)*7

if v <= 80:
    print('\033[32m Tenha um bom dia!Dirija com segurança!\033[m')
else:
    print('\033[1;31m MULTADO! Você excedeu a velocidade maxima permitida de 80km/h !')
    print('\033[31m Você deve pagar uma multa de R${:.2f} !'.format(a))
    print('\033[32m Tenha um bom dia! Dirija com segurança!')