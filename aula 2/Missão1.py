numero1 = int(input('digite o primeiro número inteiro: '))
numero2 = int(input('digite o segundo número inteiro: '))
numero3 = int(input(' digite o terceiro número inteiro:'))

if numero1 > numero2 and numero1 > numero3:
    print('O maior número é', numero1)
elif numero2 < numero1 and numero2 < numero3:
        print('o menor número é :'< numero2)
elif numero3 < numero1 and numero3 < numero2:
            print('o menor número é:', numero3)
if numero1 > numero2    and numero1 < numero3 or numero1 < numero2 and numero1 > numero3:
    print(' O número do meio é:',numero1)
elif numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero2 > numero3:
        print(' o numero do meio é:',numero2)
elif numero3 > numero1 and numero3 < numero2 or numero3 < numero1 and numero3 > numero2:
            print('o número do meio é:', numero3)
if numero1 > numero2 and numero1 > numero3:
    print(' o maior número é:',numero1)
elif numero2 > numero1 and numero2 > numero3:
        print(' o maior numero é:',numero2)
elif numero3 > numero1 and numero3 > numero2:
            print('o maior número é:',numero3)