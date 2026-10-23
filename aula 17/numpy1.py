import numpy as np 

dados_venda = np.array([12,15,17,20,22,25,28,30,35,150])

media_vendas = np.mean(dados_venda)

mediana_vendas = np.median(dados_venda)
print(f'essa é a média : {media_vendas}')
print(f'essa  é a mediana :{mediana_vendas}')

