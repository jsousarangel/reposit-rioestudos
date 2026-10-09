import pandas as pd 

df = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios.csv")

#print(df.loc[0:15 , 'id':'departamento'])
salario = df.query("salario > 300 and 'ativo' == True")
salarioNome = df[['nome', 'salario']]

print(salario)

