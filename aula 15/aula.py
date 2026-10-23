import pandas as pd

df = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios.csv")


df['liquido'] = df['lucro'] - df['salario']


df['nome'] = df['nome'].str.upper()

df['lucro'] = df['liquido'].apply(lambda x: 'lucro positivo' if x > 0 else 'lucro negativo')

print(df)

df = df.rename(columns={'liquido' : 'lucro liquido'})

