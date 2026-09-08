idade = int(input('idade: '))
tem_cnh = input(' tem cnh (s/n)? ')
if idade >= 18 and tem_cnh == 's':
    print('pode dirigir!')
else:
    print(' não pode dirigir. ')
