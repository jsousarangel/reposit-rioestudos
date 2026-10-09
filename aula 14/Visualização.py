import pandas as pd 

dfNull = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios - Null.csv")

dfNullpreenchido = dfNull

dfNullpreenchido = dfNullpreenchido.fillna({'departamento': 'nenhum', 'lucro':0})
print(dfNullpreenchido)
