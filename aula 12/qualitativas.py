import pandas as pd

df =pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios.csv")

df_id = df['id']
df_nome = df['nome']
df_departamento = df['departamento']
df_ativo = df['ativo']
df_data_de_nascimento = df['data de nascimento'] 
print

