print('Registre-se:')
usuario = input('Digite um nome usuário:')
senha =  input('Crie uma senha:')
print("\n" * 300)
loguin = input('Fazer loguin? S/N:')
if loguin == 'n':
    print('Até logo!')
while True:
    if loguin == 's':
        usua = input('Digite o usuário de login:')
    if usua != usuario:
        print('Usuário inválido!')
        break
    if usua == usuario:
        print('Usuário já cadastrado!')
    if loguin == 's':
        senh = input('Digite sua senha:')
    if senh != senha:
        print('A senha está incorreta!')
        break
    if senh == senha:
        print('Login concluido!')
        print(f'Bem-vindo {usuario}, como você está ?')
    while True:
        if senh == senha:
            print('Opções:')
            print('1-Calculadora')
            print('2-Baskhara')
            print('3-Espada')
            print('0-Sair')
            opcao = input('Digite uma opção:')
            if opcao == '0':
                print('Fechando login e saindo...')
                break

        if opcao == '1':
            print('_______')
            print('1- Soma')
            print('2- Subtração')
            print('3- Multiplicação')
            print('4- Divisão')
            print('0- Sair')
            print('_______')
            opca = input("Digite uma opção:")

            if opca == '1':
                n1 = int(input('Digite um número:'))
                n2 = int(input('Digite outro número:'))
                print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')

            if opca == '2':
                n1 = int(input('Digite um número:'))
                n2 = int(input('Digite outro número:'))
                print(f'A subtração entre {n1} e {n2} é igual a {n1 - n2}')

            if opca == '3':
                n1 = int(input('Digite um número:'))
                n2 = int(input('Digite outro número:'))
                print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}')

            if opca == '4':
                n1 = int(input('Digite um número:'))
                n2 = int(input('Digite outro número:'))
                print(f'A divisão entre {n1} e {n2} é igual a {n1 / n2}')

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
            print('[==[===========>')