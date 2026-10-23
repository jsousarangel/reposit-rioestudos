import pandas as pd 

df = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios.csv")

df = df.sort_values('salario')

df = df.sort_values('salario', ascending=False)
df = df.sort_values(['salario', 'lucro'])

print(df)