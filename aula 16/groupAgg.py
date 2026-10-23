import pandas as pd 

df = pd.read_csv(r"C:\Users\juan.rangel\Documents\aulas\dados\funcionarios.csv")

resultado = df.groupby(['departamento', 'ativo']).size()

resultado = df.groupby('departamento').agg(
    quantidade_funcionarios=('id','count'),
    salario_medio= ('salario','mean'),
    maior_salario=('salario', 'max'),
    lucro_total= ('lucro','sum')
)

print(resultado.round(2))