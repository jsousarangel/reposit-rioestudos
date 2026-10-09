import pandas as pd 

dc = { "nome": [ 'joana', 'kaio', 'marcela'], 'cargo': ['gerente', 'analista de dados', 'coordenadora'], 'salário': [7000,6500,5000]
}

df = pd.DataFrame(dc)

print(df)

df.to_csv('funcionários.csv', index=False, sep=';')