import numpy as np

#carregando um dataset
dataset = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

# exer 1
# Mostre qual a média de idade dos clientes presentes neste dataset;

idade = np.array(dataset[1:, 1], dtype=float)
media_idade = np.mean(idade)
print('EXERCICIO 1')
print(round(media_idade, 2))

print('=============================================================')

#exer 2
#Mostre quantos clientes gastaram US$100 ou mais em compras;

Gasto = np.sum(np.array(dataset[1:, 5] >= '100'))#soma dos gastos >=100
print('EXERCICIO 2')
print(Gasto)

print('=============================================================')

#exer3
#Mostre qual é a porcentagem de vendas do item menos vendido da loja;

venda = (dataset[1:, 3])#percorrendo todas as vendas
total_vendas = len(venda)#calculando o toal de venda
menor_item = np.argmin(venda)#pegando meno item
porcentagem = (menor_item*100)/total_vendas
print('EXERCICIO 3')
print(round(porcentagem, 2))

print('===========================================================')

#exer4
# Mostre qual a porcentagem de compras realizadas com o método de pagamento Venmo;
compra = dataset[1:, 16]#percorrer tadas as compras
total_compra = len(compra)#total de compra
pagamento = np.sum(np.array(dataset[1:, 16] == 'Venmo'))#somar compra = venmo
porcentagem = (pagamento*100)/total_compra
print('EXERCICIO 4')
print(round(porcentagem, 2))

print('============================================================')

#exer 5
#Mostre qual a cor de roupa mais popular no verão segundo este dataset

cor = dataset[1:, 8] #percorre cor
estacao_verao = dataset[1:, 9]#percorre estação
verao= np.where(estacao_verao == 'Summer')#ecnotra indice onde a condiçao e vdd
maior = np.argmax(cor[verao])
cormaior= cor[verao][maior]
print('EXERCICIO 5')
print(cormaior)