import pandas as pd

dados = {
'cargos': ['assistente', 'auxiliar', 'gerente'],
'salários': [2500, 1800, 7000]
}

dados_bi = pd.DataFrame(dados)

print(dados_bi.head(2))
print(dados_bi.shape)
print(dados_bi.describe())