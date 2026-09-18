turma = []

for i in range(5):
    turma.append({"nome": input(' Digite o nome do aluno: ')})
    nota1 = float(input('Digite a sua 1º nota:  '))
    nota2 = float(input('Digite a sua 2º nota:  '))

    media = ( nota1 + nota2/ 2 )
    turma[i].update({"media":media})
    if turma[i]["media"] >= 7:
        turma[i].update({"status": "aprovado!"})
    elif media >= 5 and media <= 6.9:
        turma[i].update({"status": "recuperação!" })
    else:
        turma[i].update({"status": "reprovado!" })

print(turma)

for i in range(5):
    print("nome do aluno: ", turma[i]["nome"])
    print("média do aluno: ", turma[i]["media"])
    print("status do aluno: ", turma[i]["status"])