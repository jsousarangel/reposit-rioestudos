import pandas as pd 

df1 = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios.csv")
df2 = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios_v2.csv")

resultado_final = pd.concat([df1, df2])

print(resultado_final)