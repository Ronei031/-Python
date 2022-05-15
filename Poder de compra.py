
casa = float(input('Qual o valor da casa?' ))
sal = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos vai ser pago? '))

prestacao = casa/(12*anos)

if prestacao > sal*0.30:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}! '.format(casa, anos, prestacao))
    print('Emprestimo negado!')
elif prestacao <= sal*0.30:
    print('Emprestimo aprovado!')
