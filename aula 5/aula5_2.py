comando = input("digite um comando - oi  - tchau - ajuda ")

match comando:
    case 'oi':
        print(" Olá como posso ajudar ?")
    case 'tchau':
        print('Até mais! ')
    case 'ajuda':
        print('comandos: oi - tchau - ajuda')
    case _: 
        print('Comando não reconhecido!')
comando2 = input ("Você quer ver nosso cardápio? Digite sim - não  ")
match comando2:
    case 'sim':
        print(' PIZZA DE CALABRESA: 25R$ ' )
        print(' PIZZA DE FRANGO COM CATUPIRY: 40R$ ' )
        print(' PIZZA DE PEPERONI: 30R$ ' )
    case 'não':
        print(' porque o senhor não quer o cardápio ?')
comando3 = input('Qual das nossas saborosas pizzas você gostaria de comer hojê? calabresa - frango com catupiry - peperoni '  )
match comando3:
    case 'calabresa' | 'frango com catupiry' | 'peperoni':
        print(' ótima escolha!')

