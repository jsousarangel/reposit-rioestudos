import pandas as pd 

df = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios.csv")

df['salario maior 5000'] = df['salario'].apply(lambda x: 'acima de 5mil' if x > 5000 else ' abaixo de 5mil')

df= df['ativo' == True]

df = df.rename(columns={'ativo' : 'empregado'})

print(df)