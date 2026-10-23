import pandas as pd 
import numpy as np 

df  = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios.csv")

lucro = df['lucro'].to_numpy()
print(lucro)

q1 = np.percentile(lucro,25)
q2 = np.percentile(lucro,50)
q3 = np.percentile(lucro,75)

i = q3 - q1 

limite_inferior = q1 - 1.5* i

limite_max = q3 + 1.5 *i

outliers = lucro[(lucro < limite_inferior) | (lucro > limite_max)]
dentro = lucro[(lucro >= limite_inferior) & (lucro <= limite_max )]
bigode_inf = dentro.min()
bigode_sup = dentro.max()

print(f'quartil 1(25%): {q1}')
print(f'quartil 2 (50%): {q2}')
print(f'quartil 3 (75%): {q3}')
print(f'limite inferior: {limite_inferior}')
print(f' limite máximo: {limite_max}')
print(f'outliers: {outliers}')
print(f'bigode inferior: {bigode_inf}')
print(bigode_sup)
