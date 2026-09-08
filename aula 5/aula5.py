print('1 - cadastrar 2 - listar 3 - sair ')

opcao = int(input('digite a opção desejada: '))

match opcao:
    case 1: 
        print(" você escolheu cadastrar! ")
    case 2: 
        print('você escolheu listar!') 
    case 3:
        print(' Até logo!')
    case _: 
        print(" opção inválida! ")           