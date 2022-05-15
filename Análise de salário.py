s = float(input('Digite seu salário: R$ '))
if s <= 1250:
    a = s+(1.5*100)
    print('O salário foi para R${:.2f}! '.format(a))
else:
    b = s+(1*100)
    print('O salário foi para R${:.2f}!' .format(b))

print('-=-'*15)




