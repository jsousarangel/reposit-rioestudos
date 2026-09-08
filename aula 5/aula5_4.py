nota = float(input(' Digite a nota: '))
match nota:
    case nota if nota >= 90 and nota <= 100:
        print(' Conceito A - Excelente !')
    case nota if nota >= 80 and nota <= 100:
        print(' Conceito B - Bom !')
    case nota if nota >= 70 and nota <= 100:
        print(' Conceito C - Regular ')
    case _:
        print('Nota colocada é incorreta!')
               