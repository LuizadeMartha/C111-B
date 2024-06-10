import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#carregando um dataset
dataset = pd.read_csv('nike.csv', delimiter=';')
#imprimindo nome das colunas
print(dataset.columns)
print()

#exercico 1
# Tarefa: Identificar o nome e o subtítulo do produto com o preço mais alto.
# Saída: Imprimir o nome e o subtítulo do produto com o preço máximo.
print('Exercicio1')
print(dataset.head())

preco = dataset['price']
filtrarprecoalto = preco == preco.max()

infos = dataset[['name','sub_title','price']]
prodinfos = infos[filtrarprecoalto]
nome = prodinfos['name']
titulo = prodinfos['sub_title']
precoprofuto = prodinfos['price']
print(f'Nome: {nome[68]}, sub_titulo: {titulo[68]}')
print(filtrarprecoalto)


#exercico
print('Exercicio2')
#Calcular o preço médio dos produtos que contêm "Set" no subtítulo.

subtitle = dataset['sub_title']
filtarset = subtitle.str.contains('Set')
precoset = preco[filtarset]

print(precoset)
mediaprodutos= precoset.median()
print(f'preco medio : {mediaprodutos}')


#exercico3
print('Exercicio3')
#Determinar a porcentagem de produtos que não são pretos.

corcoluna = dataset['color']
filtacolunapetados = corcoluna.str.contains('black').to_list()
newColorBlackFiltering = []
for element in filtacolunapetados:
    if element == True:
        newColorBlackFiltering.append(False)
    else:
        newColorBlackFiltering.append(True)

notBlackProducts = len(dataset[newColorBlackFiltering])

numProducts = len(dataset)

print(f'Percentage: {100 * float(notBlackProducts)/numProducts} %')

#exercicio4
print('Exercicio4')
#Listar os nomes dos produtos "Air Jordan" que estão fora de estoque.
nomeprodutos = dataset['name']
filtarnome = nomeprodutos.str.contains('Air Jordan')

airjodan = dataset[['name', 'availability']][filtarnome]
airjordanfiltro = airjodan['availability'].str.contains('OutOfStock')
airJordanNotAvailable = airjodan[airjordanfiltro]
print(airJordanNotAvailable['name'])