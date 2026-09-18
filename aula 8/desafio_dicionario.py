dicionario = {}

dicionario.update({"nome": input(' Digite o seu nome: ')})

nota1 = float(input('Digite a sua 2º nota:  '))
nota2 = float(input('Digite a sua 1º nota:  '))
media = ( nota1 + nota2/ 2 )


dicionario.update({"media": media})

print('sua média foi: ', media)

if media >= 7:
    dicionario.update({"status": "aprovado!" })
elif media >= 5 and media <= 6.9:
   dicionario.update({"status": "recuperação!" })
else:
    dicionario.update({"status": "reprovado!" })

print(dicionario["status"])





