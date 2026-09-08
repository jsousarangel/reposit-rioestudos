animal = input  ('Digite o nome de um animal: ')

match animal:
    case 'cachorro' | "gato":
        print('É um animal doméstico!')
    case 'leão' | 'tigre':
        print('É um animal selvagem!')
    case _:
        print(" Digite um animal válido")   
