import pandas as pd

df = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios.csv")

df_nome = df('salario')
df_lucro = df('lucro')

print(df)