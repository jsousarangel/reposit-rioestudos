participantes =[]

def calc_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc <= 16.9:
        print("muito abaixo do peso")
    elif imc >= 17 and imc <= 18.4:
        print('abaixo do peso!')
    elif imc >= 18.5 and  imc <= 24.9:
        print('peso normal')
    elif imc >= 25 and imc <= 29.9:
        print(' acima do peso')
    elif imc >= 30 and imc <= 34.9:
        print('obesidade grau 1')
    elif imc >= 35 and imc <= 40:
        print('obesidade grau 2 ')
    elif imc >= 40:
        print(' obesidade grau 3')
    else:
        print('você não existe bro')
        return imc



controlador = 1
while controlador == 1:
    try:
        peso = float(input("Digite  o seu peso(somente o peso): "))
        altura = float(input("Digite  o sua altura(somente a altura): "))
    except ValueError:
        print('ERRO! coloque um valor correto!')

        calc_imc(peso,altura)
    except ZeroDivisionError:
        print('Não coloque zero,ser inexistente!')
    else:   
        imc = calc_imc(peso,altura) 
        print(f'seu imc é: {imc}')
        print('Você deseja testar mais alguém ? \n Digite 1 para sim e 0 para não')
        controlador = int(input(''))
    finally:
        print('fim do programa!')
