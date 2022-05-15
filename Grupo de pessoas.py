from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de seu nascimento: '))
idade = atual-nasc
print('O atleta nasceu no ano {}, tem {} anos, e pertence ao grupo de :' .format(nasc, idade))

if idade <= 9:
    print('Atleta Mirim')
elif idade  <= 14:
    print('Atleta Infantil. ')
elif idade <= 19:
    print('Atleta Junior. ')
elif idade <=25:
    print('Atleta sênior. ')
else:
    print('Atleta Master')




