import numpy as np 

dados_venda = np.array([12,15,17,20,22,25,28,30,35,150])


q1 = np.percentile(dados_venda,25)
q2 = np.percentile(dados_venda,50)
q3 = np.percentile(dados_venda,75)

i = q3 - q1 

limite_inferior = q1 - 1.5* i

limite_max = q3 + 1.5 *i

outliers = dados_venda[(dados_venda < limite_inferior) | (dados_venda > limite_max)]
dentro = dados_venda[( dados_venda >= limite_max) & (dados_venda <= limite_max )]
bigode_inf = dentro.min()
bigode_sup = dentro.max()

print(f'quartil 1(25%): {q1}')
print(f'quartil 2 (50%): {q2}')
print(f'quartil 3 (75%): {q3}')
print(limite_inferior)
print(limite_max)
print(outliers)
print(bigode_inf)
print(bigode_sup)

