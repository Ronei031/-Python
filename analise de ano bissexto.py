from datetime import date

ano = int(input('Qual ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('-=-'*8)
    print('O ano é bissexto. '.format(ano))
else:
    print('O ano não e bissexto. ')
print('-=-'*8)
