import pandas as pd


# Ler o arquivo
x = pd.read_csv(r"DadosEmpresa.csv")

# Print das colunas do arquivo
x.info()

# Print das primeiras linhas (no caso, 10 linhas)
print(x[0:10])

# Print do total de empresas que tem a opcao_pelo_simples como SIM
print(len(x[x.opcao_pelo_simples == 'SIM']))

# Print da soma do total de capital_social de todas as empresas
print(x['capital_social'].sum())

# Print de todas as empresas que tem o capital social entre 10000 e 20000
print(x[(x['capital_social']>10000) & (x['capital_social']<20000)])

# Ler o arquivo DadosEndereco
y = pd.read_csv(r"DadosEndereco.csv")

# Fazer um merge entre os dois arquivos csv e salvar com apenas empresas que sao de curitiba
z = pd.merge(x,y, how='inner', on='cnpj')
df = z[z.values == 'CURITIBA']
df.to_csv('todas_empresas_curitiba.csv')
