import pandas as pd

df = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios.csv")

df_funcionario_sem_lucro =df[(df['lucro'] != 0) & (df['ativo'] == True)]


funcionarios_vendas = df[(df['ativo'] == True) & (df['departamento'] == 'vendas')]
print(funcionarios_vendas)

lucro_5000 = df[(df['lucro'] >= 5000)]
print(lucro_5000)

inativos = df[(df['ativo'] == False)]

df.to_csv('funcionarios4', index=False, sep=';')
