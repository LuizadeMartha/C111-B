import numpy as np
import pandas as pd

dataset = pd.read_csv('paises.csv', delimiter=';')
print(dataset.head(0))

# Exercicio 1
print('Exercicio 1a')

paisesOceania = dataset.loc[dataset['Region'].str.contains("OCEANIA")]
print(paisesOceania['Country'])
print("----------------------------------------------------------------------------")

quantPaisesOceania = len(paisesOceania['Country'])
print(f"Ha {quantPaisesOceania} paises da Oceania.")
print('-----------------------------------------------------------------------------')

# Exercicio 2
print('Exercicio 2')

worldLiteracy = dataset.iloc[:,9]
serie_worldLiteracy = pd.Series(worldLiteracy)
print(serie_worldLiteracy.mean())

print('-------------------------------------------------------------------------------')

#Exercicio 3

indice = dataset['Population'].idxmax()
regiao = dataset['Region'].values[indice]
pais = dataset['Country'].values[indice]
maiorPopulacao = dataset['Population'].values[indice]

print(f" O pais com a maior populcao e a {pais}, que se localiza na {regiao}. A {pais} conta com uma população de {maiorPopulacao} habitantes.")
print('=================================================================================================')

# Exercicio 4
p_SemCosta = dataset.loc[dataset['Coastline (coast/area ratio)'] == 0]
paisesSemCosta = p_SemCosta ['Country']
print(paisesSemCosta)
paisesSemCosta.to_csv('paisesSemCosta.csv', sep=';', header=False)