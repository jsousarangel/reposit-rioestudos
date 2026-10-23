import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [25, 30, 35]
})

df2 = pd.DataFrame({
    'id': [4, 5, 6],
    'nome': ['Diana', 'Eduardo', 'Fernanda'],
    'idade': [28, 32, 40]
})

df_notas = pd.DataFrame({
    'matematica': [8.5, 7.0, 9.0],
    'portugues':  [7.5, 8.0, 6.5]
})



vendas = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4],
    'produto':    ['Notebook', 'Mouse', 'Teclado', 'Monitor']
})

clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 5],
    'nome':       ['Ana', 'Bruno', 'Carlos', 'Eva'],
    'cidade':     ['SP', 'RJ', 'MG', 'BA']
})

resultado_merge = pd.merge(vendas, clientes, on='id_cliente')

print(resultado_merge)