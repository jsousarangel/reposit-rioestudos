import pandas as pd

df = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios.csv")

df.groupby('departamento').agg(media_salarios=('salario','mean').round(1))
                            


print(df.groupby('departamento').agg(media_salarios=('salario','mean').round(1)))