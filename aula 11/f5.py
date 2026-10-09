import pandas as pd

df = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios.csv")


funcionarios_vendas = df[(df['ativo'] == True) & (df['departamento'] == 'Vendas')]
print(funcionarios_vendas)

lucro_5000 = df[(df['lucro'] > 5000)]
print(lucro_5000)

inativos = df[(df['ativo'] == False)]
print(inativos)

funcionarios_vendas.to_csv('funcionarios_vendas.csv', index=False, sep=';')

lucro_5000.to_csv('funcionarios_com_lucro_maior5000.csv', index=False, sep=';')

inativos.to_csv('funcionarios_inativos.csv', index=False , sep=';')