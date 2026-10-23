import pandas as pd 
import numpy as np 


dfnull = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios - Null.csv")

print(dfnull.isna().sum())

dfnull = dfnull.fillna({'departamento': 'nenhum', 'lucro': 0}) 

lucro = dfnull['lucro'].to_numpy()

salario = dfnull['salario'].to_numpy()

q1 = np.percentile(coluna, 25)
q2 = np.percentile(lucro, 50)
q3 = np.percentile(lucro, 75)

print(f'primeiro quartil:{q1}')
print(f'segundo quartil: {q2}')
print(f'terceiro quartil: {q3}')

i = q3 - q1

Limite_inf = q1 - 1.5 * i

Limite_max = q3 + 1.5 * i

outliers = lucro[(lucro < Limite_inf) | (lucro > Limite_max)]

dentro = lucro[(lucro >= Limite_inf) & (lucro <= Limite_max)]
bigode_inf = dentro.min()
bigode_max = dentro.max()

print(f'limite inferior:{Limite_inf}')
print(f'limite maximo:{Limite_max}')
print(f'outliers:{outliers}')
print(f'bigode inferior:{bigode_inf}')
print(f'bigode superior: {bigode_max}')















