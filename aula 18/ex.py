import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios.csv")

print(df)

lucro = df["lucro"].to_numpy()

print(lucro)

q1 = np.percentile(lucro, 25)
q2 = np.percentile(lucro, 50)
q3 = np.percentile(lucro, 75)

print("Primeiro Quartil\n")
print(q1)
print("\nMediana\n")
print(q2)
print("\nTerceiro Quartil\n")
print(q3)

i = q3 - q1
Limite_inferior = q1 - 1.5 * i

Limite_max = q3 + 1.5 * i

outliers = lucro[(lucro < Limite_inferior) | (lucro > Limite_max)]

dentro = lucro[(lucro >= Limite_inferior) & (lucro <= Limite_max)]
bigode_inf = dentro.min()
bigode_sup = dentro.max()

print("Limite inferior: \n")
print(Limite_inferior)
print("\nLimite Superior: \n")
print(Limite_max)
print("\nOutliers: \n")
print(outliers)
print("\nBigode inferior: \n")
print(bigode_inf)
print("\nbigode superior: \n")
print(bigode_sup)

''''import pandas as pd

dfNull = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios - Null.csv")


dfNullRemovido = dfNull.dropna(subset=['departamento'])
dfNullpreenchidotodos = dfNull.fillna('nenhum')
dfNullpreenchidodepartamento = dfNull
dfNullpreenchidodepartamento['departamento'] = dfNull['departamento'].fillna('nenhum')
dfNullpreenchidodepartamento['lucro'] = dfNullpreenchidodepartamento['lucro'].fillna(0)

print(dfNullpreenchidotodos)
print('\n')
print(dfNullpreenchidodepartamento)'''

''''''''''import pandas as pd

df = pd.read_csv(r"C:\Users\juan.rangel\Downloads\funcionarios - Null.csv")

df_dep_preenchido = df.copy()

df_lucro_removido = df.copy()

df_dep_preenchido['departamento'] = df_dep_preenchido['departamento'].fillna('nenhum')

df_lucro_removido['lucro'] = df_lucro_removido.dropna(subset=['lucro'])

print(df_dep_preenchido)

print(df_lucro_removido)'''''''''''