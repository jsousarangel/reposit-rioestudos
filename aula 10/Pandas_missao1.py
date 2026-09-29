import pandas as pd 

dados = { 'nome': ['patrick', 'marcio', 'fabio','thomas','sergio'],
        'matricula': [ 1234567, 7654321, 9856730, 4356783, 4368794],
        'endereço': ['rio de janeiro', 'são paulo', 'recife', 'bahia', 'minas gerais']}
dados_df = pd.DataFrame(dados)

print(dados_df.head(3))
print(dados_df.tail(3))