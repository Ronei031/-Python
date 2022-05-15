
print('\033[34mOlá, gostaria de contatar qual setor?\033[m')
print('1- Gerencia: ')
print('2- Caixa: ')
print('3- Expedição: ')
print('4- Estoque: ')
print('5- Transferência: ')
print('6- Frotas: ')
print('7- Portaria: ')

opcao = input('Digite a opção desejada: ')
if opcao == '1':
     print('Disque  o Ramal \033[31m8500\033[m para falar com \033[34mJosé Freire.\033[m ')
elif opcao == '2':
    print('Disque  o Ramal \033[31m8501\033[m para falar com \033[34m Elisson Moraes.\033[m ')
elif opcao =='3':
    print('Disque  o Ramal \033[31m8502\033[m para falar com \033[34m Wilton Nascimento.\033[m ')
elif opcao =='4':
    print('Disque  o Ramal \033[31m8505\033[m para falar com \033[34m Jocimar Lopes.\033[m ')
elif opcao == '5':
    print('Disque  o Ramal \033[31m8506\033[m para falar com \033[34m Kelton Luiz.\033[m ')
elif opcao == '6':
    print('Disque  o Ramal \033[31m8503\033[m para falar com \033[34m Ronei Silva.\033[m ')
elif opcao =='7':
    print('1- Dia')
    print('2- Noite')
    dianoite = input('Qual o turno da ligação?')
    if dianoite == '1':
        print('Porteiro: Almir Resende ou Diogo Nunes')
        print('Ramal: 8507')
    elif dianoite == '2':
        print('Porteiro: Jhonatas Rafael ou Marconi Leite')
        print('Ramal: 8507')



