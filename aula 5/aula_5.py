numero1 = float(input(' Digite o  primeiro número'))
numero2 = float(input('Digite o segundo número '))
print(' Digite qual tipo de operação você irá usar!')
operacao = input(" subtração:'-' adição:'+' multiplicação: '*' divisão: '/' ")
match operacao:
    case '+':
        print(numero1 + numero2)
    case '-':
        print(numero1 - numero2)
    case  '*':
        print(numero1 * numero2)
    case '/':
        print(numero1 / numero2)
    case _:
        print(' Operação inválida!')

