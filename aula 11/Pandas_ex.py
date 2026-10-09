import pandas as pd
dc = {'nome': [ 'geronimo', 'martha', 'patroclos', 'tiberios', 'janaina', 'mercedes'],
      'cargo': [ 'gerente', 'gerente', 'vendedor', 'secretario', 'vendedora', 'vendedor'],
      'salario': [9600.56, 9600.56, 2600.90, 4500.45,2600.90,2600.90]}
df = pd.DataFrame(dc)

print([df ['salario'] >3000])

print(df[df ['cargo'] == 'vendedor'])
print(df[(df['cargo'] == 'vendedor') | (df['cargo'] == 'vendedora')])

df.to_csv('funcionario2.csv', index=False, sep=';')
