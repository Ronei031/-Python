from math import pow
from math import sqrt
from time import sleep

print('\033[4;34m Registre-se \033[m :')
usuario = input('Digite um nome de usuário:')
senha = input('Crie uma senha. ')
print('\n'*300)
login = input('\033[32m Deseja fazer login? S/N: ')
if login == 'n':
    print('Até logo!')
while True:
    if login == 's':
        print('\033[34m =-='*29)
        usua = input('\033[mDigite o nome de usuário:')
    if usua != usuario:
        print('\033[31mUsuário invalido !')
        break
    if usua == usuario:
        print('Usuário já cadastrado! ')
    if login == 's':
        senh = input('Digite sua senha: ')
    if senh != senha:
        print('\033[31mSenha inválida! ')
        break
    if senh == senha:
        print('\033[32mAutenticando...')
        sleep(3)
        print('\033[32mLogin concluido!')
        print(f'\033[34mSeja bem vindo {usuario}, espero que goste de nossas funcionalidades! ')
    while True:
        if senh == senha:
            print('\033[mOpções: ')
            print('1- Calculadora')
            print('2- Baskara')
            print('3- Creditos')
            print('0- Sair')
            opcao = input('Digite uma opção:')

            if opcao == '0':
                print('Fechando login e saindo....')
                sleep(3)
                break

        if opcao == '1':
            print('1- Soma: ')
            print('2- Subtrção: ')
            print('3- Multiplicação ')
            print('4- Divisão: ')
            print('5- Raiz ')
            print('6- Potencia ')
            print('0- Sair')

            opca = (input('Escolha uma opção: '))
            if opca == '1':
                v1 = int(input('Digite um número: '))
                v2 = int(input('Digite outro número: '))
                print('\033[32mA soma entre {} e {} é igual a {}! \033[m'.format(v1, v2, (v1+v2)))
                print("=-="*29)

            if opca == '2':
                n1 = int(input('Digite um numero: '))
                n2 = int(input('Digite outro numero: '))
                print('\033[32m A subtração ente {} e {} é igual a {}! \033[m'.format(n1, n2, (n1-n2)))
                print("=-=" * 29)

            if opca == '3':
                r1 = int(input('Digite um numero: '))
                r2 = int(input('Digite outro numero:'))
                print('\033[32mA multiplicação ente {} e {} é igual a {} \033[m'.format(r1, r2, (r1*r2)))
                print("=-=" * 29)

            if opca =='4':
                l1 = int(input('Digite um numero: '))
                l2 = int(input('Digite outro numero: '))
                print('\033[32mA divisão entre {} e {} é igual a {}! \033[m'.format(l1, l2, (l1/l2)))
                print("=-=" * 29)

            if opca == '5':
                r = int(input('Digite o número que deseja a raiz: '))
                print('\033[32m A raiz do numero {} é igual a {} \033[32m'.format(r, sqrt(r)))
                print("=-=" * 29)

            if opca == '6':
                x = int(input('Digite um número: '))
                y = int(input('Digite outro número: '))
                print('\033[32m A potencia entre {} e {} é igual a {} !\033[m'.format(x, y, pow(x, y)))
                print("\033[m=-=" * 29)

        if opcao == '2':
            a = int(input('Digite o Valor de A:'))
            b = int(input('Digite o Valor de B:'))
            c = int(input('Digite o Valor de C:'))

            Delta = (b * b) - 4 * a * c
            x1 = -b + Delta ** (1 / 2)
            x12 = x1 / 2 * a
            x2 = -b - Delta ** (1 / 2)
            x22 = x2 / 2 * a
            xv = -b / 2 * a
            yv = -Delta / 4 * a

            print(f'Valor de Delta={Delta}, Valor do X1={x12} e X2={x22}, XV={xv} e o YV={yv}.')

        if opcao == '3':
            print('\033[1;34m-=-=-=-=-=-=-=DESENVOLVIDO POR-=-=-=-=-=-=-=')
            print('\033[1;31mRonei Ritchele da Silva')






















