import pandas as pd

dfNull = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios - Null.csv")


dfNullRemovido = dfNull.dropna(subset=['departamento'])
dfNullpreenchidotodos = dfNull.fillna('nenhum')
dfNullpreenchidodepartamento = dfNull
dfNullpreenchidodepartamento['departamento'] = dfNull['departamento'].fillna('nenhum')
dfNullpreenchidodepartamento['lucro'] = dfNullpreenchidodepartamento['lucro'].fillna(0)

print(dfNullpreenchidotodos)
print('\n')
print(dfNullpreenchidodepartamento)
