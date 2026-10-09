import pandas as pd
dicionario = { "nome": ["joão", "maria", "pedro"], "idade": [12,10,11], 'nota': [7.0,5.6,9.0]}
df = pd.DataFrame(dicionario)

print(df)

df.to_csv('alunos.csv', index=False, sep=';')