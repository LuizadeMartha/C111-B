import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#SCATTER PLOT
#carregando um dataset
dataset = pd.read_csv('space.csv', delimiter=';')
dataset1 = pd.read_csv('paises.csv', delimiter=';')
#imprimindo nome das colunas
print(dataset.columns)
print()
print(dataset1.columns)
print()


#exercico 1

print(dataset.head())

#EXTRAI DADOS DA LOCALIZAÇÃO/ COMPARARA SE É DOS USA/ CHINA
locationColumn = dataset['Location']
USA = locationColumn.str.contains('USA')
China = locationColumn.str.contains('China')

#EXTRAI DADOS DA COMPANIA
companyColumn = dataset['Company Name']
companiesUSA = companyColumn[USA].unique()
companiesChina = companyColumn[China].unique()

print('--------------------Question 1--------------------')
print('companies USA:',companiesUSA)
print('companies CHINA:',companiesChina)

plt.bar(['USA','China'], [companiesUSA.size,companiesChina.size], color='red')
plt.title('Quantidade de empresas nos EUA e China')
plt.show()


#exercicio 2
print(dataset1.head())

#Pega dados da coluna regian / filtra de é da america do norte
regiaoColumn = dataset1['Region']
AmericadoNorte = regiaoColumn.str.contains('NORTHERN AMERICA')


taxaColumn = dataset1[['Country', 'Deathrate', 'Birthrate']]
taxanaAmerica = taxaColumn[AmericadoNorte]

plt.plot(taxanaAmerica['Country'], taxanaAmerica['Deathrate'], color='red')
plt.plot(taxanaAmerica['Country'], taxanaAmerica['Birthrate'], color='green')
plt.legend(['Deathrate', 'Birthrate'])
plt.title('Deathrate and Birthrate')
plt.show()