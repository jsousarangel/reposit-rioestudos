def calc_soma(num1,num2):
    soma = num1 + num2
    return soma

try:
    numero1 = int(input(' digite o primeiro número: '))
    numero2 = int(input(' Digite o segundo número: '))
except ValueError:
    print('você colocou um valor incorreto, tente novamente!')
else:
    print(f'a soma dos valores é {calc_soma(numero1,numero2)}')    





