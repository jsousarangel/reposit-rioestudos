nome = input('qual é o seu nome ?')
idade = input(' qual é a sua idade ?')
idade = idade.lower().replace('anos'," ").strip()
idade = int(idade)
peso = input(' qual é o seu peso?')
peso = peso.lower().replace('kg',' kilos ').strip()
if idade >= 18:
    print(' você pode entrar em nosso estabelecimento ! ')
else:
    print(" acesso negado !")