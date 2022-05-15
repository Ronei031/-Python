km = float(input('Quantos kms foram percorridos? '))
dias = int(input('Quantos dias ficou com o veículo?'))
diaria = dias*60
vk = km*0.15
print('O valor total que deve ser pago é R${:.2f} !'.format(diaria+vk))
