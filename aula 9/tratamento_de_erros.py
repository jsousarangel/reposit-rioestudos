try:
    numero = float(input('Digite um número:'))
except(Exception):
    print('erro, múmero não digitado!')
else:
    print(f'Você digitou o número: {numero}')
finally:
    print('fim do programa')